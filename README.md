# Sun'iy Intellekt Asoslari

O'quv platformasi — Django + Tailwind CSS + Alpine.js

## O'rnatish

```bash
# Virtual muhit yaratish
python -m venv venv
venv\Scripts\activate  # Windows
# source venv/bin/activate  # Linux/Mac

# Kutubxonalarni o'rnatish
pip install -r requirements.txt

# .env faylni sozlash
copy .env.example .env  # Windows
# cp .env.example .env  # Linux/Mac
# SECRET_KEY ni o'zgartiring

# Ma'lumotlar bazasini yaratish
python manage.py migrate

# Admin foydalanuvchi yaratish
python manage.py createsuperuser

# Serverni ishga tushirish
python manage.py runserver
```

## Foydalanish

1. http://localhost:8000 — Asosiy sayt
2. http://localhost:8000/admin/ — Admin panel

### Admin paneldan kontent qo'shish:

1. **Kategoriyalar** qo'shing (masalan: slug=`maruza`, name=`Ma'ruza mashg'ulotlari`)
2. **Fanlar** qo'shing (masalan: Sun'iy intellekt asoslari)
3. **Slayderlar** qo'shing (rasm bilan)
4. **Materiallar** qo'shing (PDF fayl yoki video URL bilan)
5. **Testlar** yarating, savollar va variantlar qo'shing

### Kerakli kategoriya slug'lari:

| Slug | Nomi |
|------|------|
| maruza | Ma'ruza mashg'ulotlari |
| video | Video darslar |
| amaliy | Amaliy mashg'ulotlar |
| laboratoriya | Laboratoriya mashg'ulotlari |
| taqdimot | Taqdimotlar |
| nazorat | Nazorat savollari |
| mehyoriy-hujjatlar | Me'yoriy hujjatlar |
| mashgulot-ishlanmalari | Mashg'ulot ishlanmalari |
| pedagogik-texnologiyalar | Pedagogik texnologiyalar |
| baholash-mezonlari | Baholash mezonlari |
| maslahat-va-tavsiyalar | Maslahat va tavsiyalar |
| tarqatma-materiallar | Tarqatma materiallar |

## Texnologiyalar

- Django 4.2
- Tailwind CSS (CDN)
- Alpine.js
- Jazzmin (admin tema)
- SQLite (dev) / PostgreSQL (prod)
