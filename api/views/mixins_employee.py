from ..serializer import EmployeeSerializer
from rest_framework import mixins, generics
from employees.models import Employee


# This class-based view handles listing all employees and creating a new one
# It uses DRF's mixins to simplify common CRUD operations
class Employees(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = Employee.objects.all()  # Get all Employee records from the database
    serializer_class = EmployeeSerializer  # Use EmployeeSerializer to convert data to/from JSON

    # Handle GET request: return list of all employees
    def get(self, request):
        return self.list(request)  # Uses ListModelMixin’s built-in list() method
    
    # Handle POST request: create a new employee
    def post(self, request):
        return self.create(request)  # Uses CreateModelMixin’s built-in create() method
    
class EmployeeDetail(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView,mixins.DestroyModelMixin, mixins.UpdateModelMixin,):
    queryset = Employee.objects.all()  # Get all Employee records from the database
    serializer_class = EmployeeSerializer  # Use EmployeeSerializer to convert data to/from JSON

    # Handle GET request: return list of all employees
    def get(self, request, pk):
        return self.list(request, pk)  # Uses ListModelMixin’s built-in list() method
    
    # Handle POST request: create a new employee
    def post(self, request, pk):
        return self.create(request, pk)  # Uses CreateModelMixin’s built-in create() method
    
    def put(self, request, pk):
        return self.update(request, pk)
    
    def delete(self, request, pk):
        return self.destroy(request, pk)