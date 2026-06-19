from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from .models import Material, Category


def material_sort_key(material):
    first_part = material.title.split('-', 1)[0].strip()
    if first_part.isdigit():
        return (0, int(first_part), material.title.lower())
    return (1, material.created_at, material.title.lower())


def course_list(request, category_slug=None):
    categories = Category.objects.all()
    materials = Material.objects.filter(is_active=True)
    current_category = None

    if category_slug:
        current_category = get_object_or_404(Category, slug=category_slug)
        materials = materials.filter(category=current_category)

    materials = sorted(materials, key=material_sort_key)
    paginator = Paginator(materials, 9)
    page = request.GET.get('page')
    materials = paginator.get_page(page)

    return render(request, 'courses/list.html', {
        'materials': materials,
        'categories': categories,
        'current_category': current_category,
    })


def course_detail(request, category_slug, pk):
    material = get_object_or_404(Material, pk=pk, is_active=True)
    related = Material.objects.filter(
        category=material.category, is_active=True
    ).exclude(pk=pk)
    related = sorted(related, key=material_sort_key)[:5]

    return render(request, 'courses/detail.html', {
        'material': material,
        'related': related,
    })
