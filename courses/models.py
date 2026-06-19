from io import BytesIO
from pathlib import Path

from django.core.files.base import ContentFile
from django.db import models


class Subject(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    description = models.TextField(blank=True)
    icon = models.CharField(max_length=50, blank=True, help_text="CSS class for icon, e.g. fas fa-brain")

    class Meta:
        verbose_name = 'Fan'
        verbose_name_plural = 'Fanlar'

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)

    CATEGORY_TYPES = [
        ('maruza', "Ma'ruza mashg'ulotlari"),
        ('video', 'Video darslar'),
        ('amaliy', "Amaliy mashg'ulotlar"),
        ('lab', "Laboratoriya mashg'ulotlari"),
        ('taqdimot', 'Taqdimotlar'),
        ('test', 'Testlar'),
        ('nazorat', 'Nazorat savollari'),
        ('mehyoriy', "Me'yoriy hujjatlar"),
        ('ishlanma', "Mashg'ulot ishlanmalari"),
        ('texnologiya', 'Pedagogik texnologiyalar'),
        ('baholash', 'Baholash mezonlari'),
        ('maslahat', 'Maslahat va tavsiyalar'),
        ('tarqatma', 'Tarqatma materiallar'),
    ]

    class Meta:
        verbose_name = 'Kategoriya'
        verbose_name_plural = 'Kategoriyalar'

    def __str__(self):
        return self.name


class Material(models.Model):
    title = models.CharField(max_length=300)
    description = models.TextField(blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='materials')
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name='materials', null=True, blank=True)
    file = models.FileField(upload_to='materials/', blank=True)
    preview_image = models.ImageField(upload_to='materials/previews/', blank=True, editable=False)
    video_url = models.URLField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Material'
        verbose_name_plural = 'Materiallar'

    def __str__(self):
        return self.title

    @property
    def file_extension(self):
        if not self.file:
            return ''
        return Path(self.file.name).suffix.lower().lstrip('.')

    @property
    def is_pdf(self):
        return self.file_extension == 'pdf'

    @property
    def is_image(self):
        return self.file_extension in {'jpg', 'jpeg', 'png', 'gif', 'webp'}

    def save(self, *args, **kwargs):
        old_file = None
        old_preview = None
        if self.pk:
            old_values = Material.objects.filter(pk=self.pk).values('file', 'preview_image').first()
            if old_values:
                old_file = old_values['file']
                old_preview = old_values['preview_image']

        super().save(*args, **kwargs)

        file_changed = old_file is not None and old_file != self.file.name
        needs_pdf_preview = self.file and self.is_pdf and (file_changed or not self.preview_image)
        should_clear_preview = (not self.file or not self.is_pdf) and self.preview_image

        if needs_pdf_preview:
            preview = self._render_pdf_preview()
            if preview:
                if old_preview and old_preview != self.preview_image.name:
                    self.preview_image.storage.delete(old_preview)
                name = f"{Path(self.file.name).stem}-preview.jpg"
                self.preview_image.save(name, ContentFile(preview), save=False)
                super().save(update_fields=['preview_image'])
        elif should_clear_preview:
            preview_name = self.preview_image.name
            self.preview_image = ''
            super().save(update_fields=['preview_image'])
            self.preview_image.storage.delete(preview_name)

    def _render_pdf_preview(self):
        try:
            import pypdfium2 as pdfium
        except ImportError:
            return None

        if not hasattr(self.file, 'path'):
            return None

        pdf = None
        page = None
        try:
            pdf = pdfium.PdfDocument(self.file.path)
            page = pdf[0]
            image = page.render(scale=1.6).to_pil()
            image.thumbnail((900, 1200))
            if image.mode != 'RGB':
                image = image.convert('RGB')

            output = BytesIO()
            image.save(output, format='JPEG', quality=86, optimize=True)
            return output.getvalue()
        except Exception:
            return None
        finally:
            if page is not None:
                page.close()
            if pdf is not None:
                pdf.close()
