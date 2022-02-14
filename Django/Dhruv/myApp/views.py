from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib.auth import logout, authenticate, login
from datetime import datetime
from myApp.models import Contact
from django.contrib import messages


# Create your views here.
# password for rathod_dhruv user dmr@#123


def index(request):
    # print(request.user)
    context = {
        'variable': "this is sent"
    }
    if request.user.is_anonymous:
        return redirect("/login")
    return render(request, 'index.html', context)  # in this field
    # return HttpResponse("this is home page")


def loginUser(request):
    if request.method == "POST":
        username = request.POST.get('user name')
        password = request.POST.get('password')
        # print(username, password)
        # check if user has entered correct credentials
        user = authenticate(username=username, password=password)
        if user is not None:
            # A backend authenticated the credentials
            login(request, user)
            return redirect("/")

        else:
            # No backend authenticated the credentials
            # change apply login.html to base
            return render(request, 'index.html')

    return render(request, 'index.html')  # change apply login.html to base


def logoutUser(request):
    logout(request)
    return redirect("/login")


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
