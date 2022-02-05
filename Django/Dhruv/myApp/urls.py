from xml.dom.minidom import Document
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from myApp import views

urlpatterns = [
    path("", views.index, name='home'),
    path("about", views.about, name='about'),
    path("services", views.services, name='services'),
    path("contact", views.contact, name='contact'),
    path("login", views.loginUser, name='login'),
    path("logout", views.logoutUser, name='logout')


]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
