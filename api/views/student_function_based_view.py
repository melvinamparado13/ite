from django.shortcuts import render
from students.models import Students
from api.serializer import StudentSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

# Create your views here.

@api_view(['GET', 'POST', 'DELETE'])
def studentView(request):
    if(request.method == 'GET'):
        students = Students.objects.all()
        serializer = StudentSerializer(students, many=True)
        print(students, serializer.data)
        return Response(serializer.data, status=status.HTTP_200_OK)
    if(request.method == 'POST'):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        print(serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    if(request.method == 'PUT'):
        id = request.data.get('id')
        try:
            student = Students.objects.get(id=id)
        except Students.DoesNotExist:
            return Response({'error': 'Student not found'}, status=status.HTTP_404_NOT_FOUND)
        serializer = StudentSerializer(student, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        print(serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    if(request.method == 'DELETE'):
        id = request.data.get('id')
        try:
            student = Students.objects.get(id=id)
        except Students.DoesNotExist:
            return Response({'error': 'Student not found'}, status=status.HTTP_404_NOT_FOUND)
        student.delete()
        return Response({'message': 'Student deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
        
@api_view(['GET', 'PUT', 'DELETE'])
def student(request, student_id):
    try:
        student = Students.objects.get(id=student_id)
    except student.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = StudentSerializer(student)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'PUT':
        serializer = StudentSerializer(student, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)