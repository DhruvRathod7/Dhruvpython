from unicodedata import name
from django.urls import path
from .import views

urlpatterns = [
    path('', views.index, name='/'),
    path('student-view/<str:pk>/', views.studentView, name="studentview"),
    path('add-student', views.studentAdd, name="studentadd"),
    path('update-student/<str:pk>/', views.studentUpdate, name="studentupdate"),
    path('delete-student/<str:pk>/', views.studentDelete, name="studentdelete"),
    path('download-excel/', views.download_excel, name="downoad-excel")
]
