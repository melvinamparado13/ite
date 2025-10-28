from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets, status
from rest_framework.response import Response
from students.models import Students
from api.serializer import StudentSerializer


class Student(viewsets.ViewSet):
    # GET /students/ → List all students
    def list(self, request):
        queryset = Students.objects.all()
        serializer = StudentSerializer(queryset, many=True)
        return Response(serializer.data)

    # POST /students/ → Create a new student
    def create(self, request):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors)

    # GET /students/{id}/ → Retrieve a specific student
    def retrieve(self, request, pk=None):
        student = get_object_or_404(Student, pk=pk)
        serializer = StudentSerializer(student)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # PUT /students/{id}/ → Update a student
    def update(self, request, pk=None):
        student = get_object_or_404(Student, pk=pk)
        serializer = StudentSerializer(student, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    # DELETE /students/{id}/ → Delete a student
    def delete(self, request, pk=None):
        student = get_object_or_404(Student, pk=pk)
        student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class StudentModelViewSet(viewsets.ModelViewSet):
    queryset = Students.objects.all()
    serializer_class = StudentSerializer
