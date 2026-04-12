import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from courses.models import Category, Subject

categories = [
    ('maruza', "Ma'ruza mashg'ulotlari"),
    ('video', 'Video darslar'),
    ('amaliy', "Amaliy mashg'ulotlar"),
    ('laboratoriya', "Laboratoriya mashg'ulotlari"),
    ('taqdimot', 'Taqdimotlar'),
    ('nazorat', 'Nazorat savollari'),
    ('mehyoriy-hujjatlar', "Me'yoriy hujjatlar"),
    ('mashgulot-ishlanmalari', "Mashg'ulot ishlanmalari"),
    ('pedagogik-texnologiyalar', 'Pedagogik texnologiyalar'),
    ('baholash-mezonlari', 'Baholash mezonlari'),
    ('maslahat-va-tavsiyalar', 'Maslahat va tavsiyalar'),
    ('tarqatma-materiallar', 'Tarqatma materiallar'),
]

for slug, name in categories:
    Category.objects.get_or_create(slug=slug, defaults={'name': name})
    print(f"  + {name}")

Subject.objects.get_or_create(
    slug='suniy-intellekt-asoslari',
    defaults={'name': "Sun'iy intellekt asoslari", 'icon': 'fas fa-brain'}
)
print("  + Fan: Sun'iy intellekt asoslari")

print("\nMa'lumotlar muvaffaqiyatli qo'shildi!")
