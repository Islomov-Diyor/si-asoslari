from django.shortcuts import render, redirect
from django.contrib import messages
from .models import ContactMessage


def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name', '').strip()
        email = request.POST.get('email', '').strip()
        message = request.POST.get('message', '').strip()

        if name and email and message:
            ContactMessage.objects.create(name=name, email=email, message=message)
            messages.success(request, "Xabaringiz muvaffaqiyatli yuborildi!")
            return redirect('contact:contact')
        else:
            messages.error(request, "Iltimos, barcha maydonlarni to'ldiring.")

    return render(request, 'contact/contact.html')
