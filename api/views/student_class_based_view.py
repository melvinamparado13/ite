from ..serializer import StudentSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from students.models import Students
from django.http import Http404


# Class-Based View to handle multiple students (list all or create new)
class Student(APIView):
    # Handle GET request: return a list of all students
    def get(self, request):
        students = Students.objects.all()  # Get all student records from the database
        serializer = StudentSerializer(students, many=True)  # Serialize (convert) data to JSON
        return Response(serializer.data, status=status.HTTP_200_OK)  # Return data with 200 OK
    
    # Handle POST request: create a new student record
    def post(self, request):
        serializer = StudentSerializer(data=request.data)  # Deserialize incoming data
        if serializer.is_valid():  # Check if data is valid
            serializer.save()  # Save new student to database
            return Response(serializer.data, status=status.HTTP_201_CREATED)  # Return created student data
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  # Return errors if invalid


# Class-Based View to handle a single student (get, update, delete)
class StudentDetail(APIView):
    # Helper function: get one student by primary key (pk)
    def get_object(self, pk):
        try:
            return Students.objects.get(pk=pk)  # Find student by ID
        except Students.DoesNotExist:
            raise Http404  # Raise 404 if student not found

    # Handle GET request: return details of a specific student
    def get(self, request, pk):
        students = self.get_object(pk=pk)  # Get student object
        serializer = StudentSerializer(students)  # Serialize the student data
        return Response(serializer.data, status=status.HTTP_200_OK)  # Send student data back

    # Handle PUT request: update student data
    def put(self, request, pk):
        student = self.get_object(pk)  # Get student to update
        serializer = StudentSerializer(student, data=request.data)  # Replace data with new input
        if serializer.is_valid():  # Check if data is valid
            serializer.save()  # Save updated data to database
            return Response(serializer.data, status=status.HTTP_200_OK)  # Return updated data
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  # Return errors if invalid

    # Handle DELETE request: remove a student
    def delete(self, request, pk):
        student = self.get_object(pk)  # Get student to delete
        student.delete()  # Delete from database
        return Response(status=status.HTTP_204_NO_CONTENT)  # Return empty response (success)
