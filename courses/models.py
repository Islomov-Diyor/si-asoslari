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
    video_url = models.URLField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Material'
        verbose_name_plural = 'Materiallar'

    def __str__(self):
        return self.title
