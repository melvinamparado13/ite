from django.shortcuts import render
from students.models import Students
from api.serializer import StudentSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

# Create your views here.

# This view handles multiple students (list all, create new, update, or delete)
@api_view(['GET', 'POST', 'DELETE'])
def studentView(request):
    # Handle GET request: return all students
    if(request.method == 'GET'):
        students = Students.objects.all()  # Get all student records
        serializer = StudentSerializer(students, many=True)  # Serialize list of students
        print(students, serializer.data)  # Print data (for debugging)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # Handle POST request: create a new student
    if(request.method == 'POST'):
        serializer = StudentSerializer(data=request.data)  # Deserialize input data
        if serializer.is_valid():  # Validate the input
            serializer.save()  # Save new student to database
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        print(serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # Handle PUT request: update existing student (based on ID in request)
    if(request.method == 'PUT'):
        id = request.data.get('id')  # Get student ID from request body
        try:
            student = Students.objects.get(id=id)  # Find student by ID
        except Students.DoesNotExist:
            return Response({'error': 'Student not found'}, status=status.HTTP_404_NOT_FOUND)
        serializer = StudentSerializer(student, data=request.data)  # Update student data
        if serializer.is_valid():
            serializer.save()  # Save updated student
            return Response(serializer.data, status=status.HTTP_200_OK)
        print(serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # Handle DELETE request: remove a student (based on ID in request)
    if(request.method == 'DELETE'):
        id = request.data.get('id')  # Get student ID
        try:
            student = Students.objects.get(id=id)  # Find student by ID
        except Students.DoesNotExist:
            return Response({'error': 'Student not found'}, status=status.HTTP_404_NOT_FOUND)
        student.delete()  # Delete student record
        return Response({'message': 'Student deleted successfully'}, status=status.HTTP_204_NO_CONTENT)


# This view handles a single student (get, update, delete) using ID in the URL
@api_view(['GET', 'PUT', 'DELETE'])
def student(request, student_id):
    try:
        student = Students.objects.get(id=student_id)  # Find student by ID
    except Students.DoesNotExist:  #  FIX: 'Students' not 'student'
        return Response(status=status.HTTP_404_NOT_FOUND)  # Return 404 if not found

    # Handle GET request: return one student's details
    if request.method == 'GET':
        serializer = StudentSerializer(student)  # Serialize single student
        return Response(serializer.data, status=status.HTTP_200_OK)

    # Handle PUT request: update one student
    elif request.method == 'PUT':
        serializer = StudentSerializer(student, data=request.data)  # Update data
        if serializer.is_valid():
            serializer.save()  # Save updated info
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # Handle DELETE request: delete a student
    elif request.method == 'DELETE':
        student.delete()  # Remove record from database
        return Response(status=status.HTTP_204_NO_CONTENT)