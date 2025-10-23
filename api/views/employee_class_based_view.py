from ..serializer import EmployeeSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from employees.models import Employee
from django.http import Http404


# Class Based View for handling multiple employees (list and create)
class Employees(APIView):
    # Handle GET request: return a list of all employees
    def get(self, request):
        employees = Employee.objects.all()  # Get all employees from the database
        serializer = EmployeeSerializer(employees, many=True)  # Convert to JSON format
        return Response(serializer.data, status=status.HTTP_200_OK)  # Send response with data
    
    # Handle POST request: create a new employee
    def post(self, request):
        serializer = EmployeeSerializer(data=request.data)  # Convert incoming data to serializer
        if serializer.is_valid():  # Check if data is valid
            serializer.save()  # Save new employee to the database
            return Response(serializer.data, status=status.HTTP_201_CREATED)  # Return created data
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  # Return validation errors


# Class Based View for handling a single employee (retrieve, update, delete)
class EmployeeDetail(APIView):
    # Helper method to get a single employee by ID (or return 404 if not found)
    def get_object(self, pk):
        try:
            return Employee.objects.get(pk=pk)
        except Employee.DoesNotExist:
            raise Http404

    # Handle GET request: return details of one employee
    def get(self, request, pk):
        employees = self.get_object(pk=pk)  # Get employee by primary key (id)
        serializer = EmployeeSerializer(employees)  # Convert to JSON format
        return Response(serializer.data, status=status.HTTP_200_OK)  # Send response with data

    # Handle PUT request: update an existing employee
    def put(self, request, pk):
        employees = self.get_object(pk)  # Get existing employee
        serializer = EmployeeSerializer(employees, data=request.data)  # Replace data with new values
        if serializer.is_valid():  # Validate new data
            serializer.save()  # Save changes to the database
            return Response(serializer.data, status=status.HTTP_200_OK)  # Return updated data
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  # Return validation errors

    # Handle DELETE request: remove an employee
    def delete(self, request, pk):
        employees = self.get_object(pk)  # Get employee to delete
        employees.delete()  # Delete from database
        return Response(status=status.HTTP_204_NO_CONTENT)  # Return empty response (success)
