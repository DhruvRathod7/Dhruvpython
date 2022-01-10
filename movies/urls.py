from django.urls import path
from . import views

# movies_collection/
# movies/1/details
urlpattern = [
    path('', views.index, name='index')
]
