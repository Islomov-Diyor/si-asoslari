from django.urls import path
from . import views

app_name = 'actions'

urlpatterns = [
    path('', views.index, name='index'),
    path('gradient/', views.gradient, name='gradient'),
    path('aktivatsiya/', views.aktivatsiya, name='aktivatsiya'),
    path('kmeans/', views.kmeans, name='kmeans'),
    path('confusion-matrix/', views.confusion_matrix, name='confusion_matrix'),
    path('regressiya/', views.regressiya, name='regressiya'),
    path('perceptron/', views.perceptron, name='perceptron'),
    path('bayes/', views.bayes, name='bayes'),
    path('knn/', views.knn, name='knn'),
    path('nlp/', views.nlp, name='nlp'),
]
