from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Student
from .serializers import StudentSerializer
from rest_framework import viewsets

# Create your views here.
class GradeViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

# def grades(request):
#     if request.method == 'GET':
#         students = Student.objects.first()
#         serializer = StudentSerializer(students)
#         return JsonResponse(serializer.data)