from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from api.models import Student

# Create your views here.
from .serializers import StudentSerializer


@api_view(['GET'])
def index(request):
    student = Student.objects.all()
    serialstudents = StudentSerializer(student, many=True)
    return Response(serialstudents.data)
