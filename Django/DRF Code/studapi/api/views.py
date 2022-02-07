from django.shortcuts import render
import io
from rest_framework.parsers import JSONParser
from api.serializers import StudentSerializer
from django.views.decorators.csrf import csrf_exempt
# from .models import Student
from .serializers import StudentSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse, JsonResponse

# Create your views here.
# Model Object - single Student Data


@csrf_exempt
def student_create(request):
    if request.method == 'POST':
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        serializer = StudentSerializer(data=pythondata)
        if serializer.is_valid():
            serializer.save()
            res = {'msg': 'Data Created'}
            json_data = JSONRenderer().render(res)
            return HttpResponse(json_data, content_type='application/json')
        json_data = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data, content_type='application/json')


# def student_detail(request, dm):
#     stu = Student.objects.get(id=dm)
#     # print(stu)
#     serializer = StudentSerializer(stu)
#     # print(serializer)
#     # print(serializer.data)
#     json_data = JSONRenderer().render(serializer.data)
#     # print(json_data)
#     return HttpResponse(json_data, content_type='application/json')
#     # return JsonResponse(serializer.data)


# Query Set - All Stdent Data

# def student_list(request):
#     stu = Student.objects.all()
#     # print(stu)
#     serializer = StudentSerializer(stu, many=True)
#     # print(serializer)
#     # print(serializer.data)
#     json_data = JSONRenderer().render(serializer.data)
#     # print(json_data)
#     return HttpResponse(json_data, content_type='application/json')
#     # return JsonResponse(serializer.data, safe=False)
