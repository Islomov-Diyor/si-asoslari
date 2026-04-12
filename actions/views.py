from django.shortcuts import render


def coming_soon(request):
    return render(request, 'actions/coming_soon.html')
