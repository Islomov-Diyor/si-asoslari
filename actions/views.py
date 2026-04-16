from django.shortcuts import render


def index(request):
    return render(request, 'actions/index.html')


def gradient(request):
    return render(request, 'actions/gradient.html')


def aktivatsiya(request):
    return render(request, 'actions/aktivatsiya.html')


def kmeans(request):
    return render(request, 'actions/kmeans.html')


def confusion_matrix(request):
    return render(request, 'actions/confusion_matrix.html')


def regressiya(request):
    return render(request, 'actions/regressiya.html')


def perceptron(request):
    return render(request, 'actions/perceptron.html')


def bayes(request):
    return render(request, 'actions/bayes.html')


def knn(request):
    return render(request, 'actions/knn.html')


def nlp(request):
    return render(request, 'actions/nlp.html')
