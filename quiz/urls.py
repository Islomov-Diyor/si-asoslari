from django.urls import path
from . import views

app_name = 'quiz'

urlpatterns = [
    path('', views.quiz_list, name='list'),
    path('<int:pk>/', views.quiz_take, name='take'),
]
