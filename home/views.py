from django.shortcuts import render
from .models import Slider
from courses.models import Subject, Material, Category


AI_TOOLS = [
    {
        'name': 'ChatGPT',
        'url': 'https://chatgpt.com/',
        'domain': 'chatgpt.com',
        'initials': 'CG',
        'accent': '#10a37f',
    },
    {
        'name': 'Claude',
        'url': 'https://claude.ai/',
        'domain': 'claude.ai',
        'initials': 'CL',
        'accent': '#d97757',
    },
    {
        'name': 'Google Gemini',
        'url': 'https://gemini.google.com/',
        'domain': 'gemini.google.com',
        'initials': 'GE',
        'accent': '#4285f4',
    },
    {
        'name': 'Microsoft Copilot',
        'url': 'https://copilot.microsoft.com/',
        'domain': 'copilot.microsoft.com',
        'initials': 'CO',
        'accent': '#7c3aed',
    },
    {
        'name': 'Perplexity',
        'url': 'https://www.perplexity.ai/',
        'domain': 'perplexity.ai',
        'initials': 'PX',
        'accent': '#20b8cd',
    },
    {
        'name': 'Midjourney',
        'url': 'https://www.midjourney.com/',
        'domain': 'midjourney.com',
        'initials': 'MJ',
        'accent': '#111827',
    },
    {
        'name': 'Runway',
        'url': 'https://runwayml.com/',
        'domain': 'runwayml.com',
        'initials': 'RW',
        'accent': '#6d5dfc',
    },
    {
        'name': 'Leonardo.Ai',
        'url': 'https://leonardo.ai/',
        'domain': 'leonardo.ai',
        'initials': 'LA',
        'accent': '#7c3aed',
    },
    {
        'name': 'Stability AI',
        'url': 'https://stability.ai/',
        'domain': 'stability.ai',
        'initials': 'SA',
        'accent': '#2563eb',
    },
    {
        'name': 'Hugging Face',
        'url': 'https://huggingface.co/',
        'domain': 'huggingface.co',
        'initials': 'HF',
        'accent': '#f5b700',
    },
    {
        'name': 'Poe',
        'url': 'https://poe.com/',
        'domain': 'poe.com',
        'initials': 'PO',
        'accent': '#5d5fef',
    },
    {
        'name': 'Canva Magic Design',
        'url': 'https://www.canva.com/magic-design/',
        'domain': 'canva.com',
        'initials': 'CA',
        'accent': '#00c4cc',
    },
    {
        'name': 'Gamma',
        'url': 'https://gamma.app/',
        'domain': 'gamma.app',
        'initials': 'GA',
        'accent': '#8b5cf6',
    },
    {
        'name': 'ElevenLabs',
        'url': 'https://elevenlabs.io/',
        'domain': 'elevenlabs.io',
        'initials': 'EL',
        'accent': '#111827',
    },
    {
        'name': 'Suno',
        'url': 'https://suno.com/',
        'domain': 'suno.com',
        'initials': 'SU',
        'accent': '#f97316',
    },
]


def home(request):
    sliders = Slider.objects.filter(is_active=True)
    subjects = Subject.objects.all()[:6]
    recent_materials = Material.objects.filter(is_active=True).order_by('-created_at')[:6]
    context = {
        'sliders': sliders,
        'subjects': subjects,
        'recent_materials': recent_materials,
        'ai_tools': AI_TOOLS,
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
