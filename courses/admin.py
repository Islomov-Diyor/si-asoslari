from django.contrib import admin
from .models import Subject, Category, Material


@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Material)
class MaterialAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'subject', 'is_active', 'created_at')
    list_filter = ('category', 'subject', 'is_active')
    search_fields = ('title', 'description')
    list_editable = ('is_active',)
