from ..serializer import EmployeeSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from employees.models import Employee
from django.http import Http404


# Class Base View
class Employees(APIView):
    def get(self, request):
        employees = Employee.objects.all()
        serializer = EmployeeSerializer(employees, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        serializer = EmployeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class EmployeeDetail(APIView):
    def get_object(self, pk):
        try:
            return Employee.objects.get(pk=pk)
        except Employee.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        employees = self.get_object(pk=pk)
        serializer = EmployeeSerializer(employees)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        employees = self.get_object(pk)
        serializer = EmployeeSerializer(employees, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        employees = self.get_object(pk)
        employees.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)