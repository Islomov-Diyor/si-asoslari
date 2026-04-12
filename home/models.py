from django.db import models


class Slider(models.Model):
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=300, blank=True)
    image = models.ImageField(upload_to='sliders/')
    cta_text = models.CharField(max_length=100, default="Batafsil")
    cta_link = models.CharField(max_length=300, default="/courses/")
    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['order']
        verbose_name = 'Slayder'
        verbose_name_plural = 'Slayderlar'

    def __str__(self):
        return self.title
