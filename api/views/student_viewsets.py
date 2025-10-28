from django.shortcuts import get_object_or_404
from rest_framework import viewsets, status
from rest_framework.response import Response

from students.models import Students
from api.serializer import StudentSerializer


# Basic ViewSet
class Student(viewsets.ViewSet):
    def list(self, request):
        queryset = Students.objects.all()
        serializer = StudentSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        student = get_object_or_404(Student, pk=pk)
        serializer = StudentSerializer(student)
        return Response(serializer.data)

    def update(self, request, pk=None):
        student = get_object_or_404(Student, pk=pk)
        serializer = StudentSerializer(student, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk=None):  # rename from delete → destroy for consistency
        student = get_object_or_404(Student, pk=pk)
        student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# ModelViewSet version (simpler)
class StudentModelViewSet(viewsets.ModelViewSet):
    queryset = Students.objects.all()
    serializer_class = StudentSerializer