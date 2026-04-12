from django.urls import path
from . import views

app_name = 'courses'

urlpatterns = [
    path('', views.course_list, name='list'),
    path('<slug:category_slug>/', views.course_list, name='category'),
    path('<slug:category_slug>/<int:pk>/', views.course_detail, name='detail'),
]
