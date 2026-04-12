from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from .models import Material, Category


def course_list(request, category_slug=None):
    categories = Category.objects.all()
    materials = Material.objects.filter(is_active=True)
    current_category = None

    if category_slug:
        current_category = get_object_or_404(Category, slug=category_slug)
        materials = materials.filter(category=current_category)

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
    ).exclude(pk=pk)[:5]

    return render(request, 'courses/detail.html', {
        'material': material,
        'related': related,
    })
