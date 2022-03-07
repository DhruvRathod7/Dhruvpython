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


@api_view(['GET'])
def studentView(request, pk):
    student = Student.objects.get(id=pk)
    serialstudent = StudentSerializer(student, many=False)
    return Response(serialstudent.data)


@api_view(['POST'])
def studentAdd(request):
    serialdata = StudentSerializer(data=request.data)
    if serialdata.is_valid():
        serialdata.save()
    return Response(serialdata.data)


@api_view(['POST'])
def studentUpdate(request, pk):
    student = Student.objects.get(id=pk)
    serialstudent = StudentSerializer(instance=student, data=request.data)
    if serialstudent.is_valid():
        serialstudent.save()
    return Response(serialstudent.data)


@api_view(['DELETE'])
def studentDelete(request, pk):
    student = Student.objects.get(id=pk)
    student.delete()

    student = Student.objects.all()
    serialstudents = StudentSerializer(student, many=True)
    return Response(serialstudents.data)
