from django.shortcuts import render, HttpResponse
from datetime import datetime
from myApp.models import Contact
from django.contrib import messages

# Create your views here.


def index(request):
    context = {
        'variable': "this is sent"
    }
    return render(request, 'index.html', context)
    # return HttpResponse("this is home page")


def about(request):
    return render(request, 'about.html')


def services(request):
    return render(request, 'services.html')


def contact(request):
    if request.method == "POST":
        if request.POST.get('name') == "":
            return render(request, 'contact.html', {'error': True})

        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        contact = Contact(name=name, email=email, phone=phone,
                          desc=desc, date=datetime.today())
        contact.save()
        messages.success(request, 'Your message has send successfully!')
    return render(request, 'contact.html')
