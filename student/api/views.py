from datetime import datetime
from pkgutil import get_data
from urllib import response
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from api.models import Student
import xlwt
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


def download_excel(request):
    response=HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="Student.xls"' 

    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Student Data')

    row_num = 0

    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    columns = ['Name', 'Email', 'Phone',]

    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)

    font_style = xlwt.XFStyle()
        
    rows = Student.objects.all().values_list('name', 'email', 'phone')

    for row in rows:
        row_num+=1
        for col_num in range(len(row)):
            ws.write(row_num, col_num, row[col_num], font_style)
            
    wb.save(response)

    return response