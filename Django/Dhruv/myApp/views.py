import re
from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib.auth import logout, authenticate, login
from datetime import datetime
from myApp.models import Contact, TableBooking
from django.contrib import messages


# Create your views here.
# password for rathod_dhruv user dmr@#123


def index(request):
    # print(request.user)
    context = {
        'variable': "this is sent"
    }
    # if request.user.is_anonymous:
    #     return redirect("/login")
    return render(request, 'index.html', context)  # in this field
    # return HttpResponse("this is home page")


# def loginUser(request):
#     if request.method == "POST":
#         username = request.POST.get('user name')
#         password = request.POST.get('password')
#         # print(username, password)
#         # check if user has entered correct credentials
#         user = authenticate(username=username, password=password)
#         if user is not None:
#             # A backend authenticated the credentials
#             login(request, user)
#             return redirect("/")

#         else:
#             # No backend authenticated the credentials
#             # change apply login.html to base
#             return render(request, 'index.html')

#     return render(request, 'index.html')  # change apply login.html to base


# def logoutUser(request):
#     logout(request)
#     return redirect("/login")


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

def handleSignup(request):
    if request.method == 'POST':
        # get the post parameters
        username = request.POST['username']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        # Check for errorneous inputs
        if len(username) > 10:
            messages.error(request, "Username must be under 10 characters")
            return redirect('home')
        if not username.isalnum():
            messages.error(request, "Username should only contain letter and numbers")
            return redirect('home')
        if pass1 != pass2:
            messages.error(request, "Passwords do not match")
            return redirect('home')

        # Create the user
        myuser = User.objects.create_user(username, email, pass1)
        myuser.save()
        messages.success(request,"your acoount has been created succesfully")
        return redirect('home')


    else:
        return HttpResponse('404 - Not Found')

def handleLogin(request):
    if request.method == 'POST':
        # get the post parameters
        loginusername = request.POST['loginusername']
        loginpassword = request.POST['loginpassword']

        user = authenticate(username=loginusername, password=loginpassword)

        if user is not None:
            login(request,user)
            messages.success(request, "Successfully Logged In")
            return redirect('home')
        else:
            messages.error(request, "Invalid Credentials, Please Try Again")
            return redirect('home')
        
    return HttpResponse('404 - Not Found')

def handleLogout(request):
    logout(request)
    messages.success(request, "Successfully Logged out")
    return redirect('home')

def tablebooking(request):
    if request.method == "POST":
        
        # get the post parameters
        username = request.POST['username']
        email = request.POST['email']
        phone = request.POST['phone']
        date = request.POST['date']
        noofpeople = request.POST['noofpeople']
        time = request.POST['time']
        tablebooking = TableBooking(username=username, email=email, phone=phone,
                          date=date, noofpeople=noofpeople, time=time)
        tablebooking.save()
        messages.success(request, 'Your Table Booked successfully!')
    
    else:
        return HttpResponse('404 - Not Found')


def icecreams(request):
    return render(request, 'icecreams.html')

def colddrinks(request):
    return render(request, 'colddrinks.html')

def familypack(request):
    return render(request, 'familypack.html')

        
        
    



