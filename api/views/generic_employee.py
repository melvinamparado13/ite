from rest_framework import generics
from employees.models import Employee
from api.serializer import EmployeeSerializer

# class Employees(generics.ListAPIView, generics.CreateAPIView, ):
#     queryset = Employee.objects.all()
#     serializer_class = EmployeeSerializer

# Option 2
class Employees(generics.ListCreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

# class EmployeeDetail(generics.RetrieveAPIView, generics.UpdateAPIView, generics.DestroyAPIView):
#     queryset = Employee.objects.all()
#     serializer_class = EmployeeSerializer
#     Lookup_field = 'pk'

# Option 2
class EmployeeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    lookup_field = 'pk'