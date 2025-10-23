from django.shortcuts import render
from employees.models import Employee
from api.serializer import EmployeeSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

# Create your views here.

# This function handles multiple operations (GET, POST, PUT, DELETE) for employees
@api_view(['GET', 'POST', 'DELETE'])
def employeeView(request):
    # Handle GET request: get all employees
    if(request.method == 'GET'):
        employees = Employee.objects.all()  # Fetch all employee records
        serializer = EmployeeSerializer(employees, many=True)  # Serialize multiple employees
        print(employees, serializer.data)  # Print for debugging (optional)
        return Response(serializer.data, status=status.HTTP_200_OK)  # Return employee data

    # Handle POST request: add a new employee
    if(request.method == 'POST'):
        serializer = EmployeeSerializer(data=request.data)  # Deserialize incoming data
        if serializer.is_valid():  # Check if data is valid
            serializer.save()  # Save new employee to database
            return Response(serializer.data, status=status.HTTP_201_CREATED)  # Return created employee data
        print(serializer.errors)  # Print validation errors (for debugging)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  # Return errors

    # Handle PUT request: update existing employee (based on ID sent in data)
    if(request.method == 'PUT'):
        id = request.data.get('id')  # Get employee ID from request body
        try:
            employee = Employee.objects.get(id=id)  # Find employee by ID
        except Employee.DoesNotExist:
            return Response({'error': 'Employee not found'}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = EmployeeSerializer(employee, data=request.data)  # Update employee data
        if serializer.is_valid():
            serializer.save()  # Save updated employee info
            return Response(serializer.data, status=status.HTTP_200_OK)
        print(serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # Handle DELETE request: remove employee (based on ID sent in data)
    if(request.method == 'DELETE'):
        id = request.data.get('id')  # Get employee ID from request body
        try:
            employee = Employee.objects.get(id=id)  # Find employee by ID
        except Employee.DoesNotExist:
            return Response({'error': 'Employee not found'}, status=status.HTTP_404_NOT_FOUND)
        
        employee.delete()  # Delete the employee record
        return Response({'message': 'Employee deleted successfully'}, status=status.HTTP_204_NO_CONTENT)


# This function handles a single employee (by ID in URL)
@api_view(['GET', 'PUT', 'DELETE'])
def employee(request, employee_id):
    try:
        employee = Employee.objects.get(id=employee_id)  # Find employee by ID
    except Employee.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)  # Return 404 if not found
    
    # Handle GET request: return one employee's details
    if request.method == 'GET':
        serializer = EmployeeSerializer(employee)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # Handle PUT request: update employee data
    elif request.method == 'PUT':
        serializer = EmployeeSerializer(employee, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # Handle DELETE request: remove the employee
    elif request.method == 'DELETE':
        employee.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
