from django.shortcuts import render
from .models import Slider
from courses.models import Subject, Material, Category


def home(request):
    sliders = Slider.objects.filter(is_active=True)
    subjects = Subject.objects.all()[:6]
    recent_materials = Material.objects.filter(is_active=True).order_by('-created_at')[:6]
    context = {
        'sliders': sliders,
        'subjects': subjects,
        'recent_materials': recent_materials,
    }
    return render(request, 'home/index.html', context)


def about(request):
    skills = [
        {'name': "Sun'iy intellekt", 'pct': 92},
        {'name': 'Machine Learning',  'pct': 88},
        {'name': 'Data Science',       'pct': 85},
        {'name': 'Python dasturlash',  'pct': 80},
        {'name': "O'qitish metodikasi", 'pct': 95},
    ]
    return render(request, 'home/about.html', {'skills': skills})
