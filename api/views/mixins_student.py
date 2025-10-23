from ..serializer import StudentSerializer
from rest_framework import mixins, generics
from students.models import Students


# This class-based view handles listing all students and creating a new one
# It uses DRF's mixins to simplify common CRUD operations
class Student(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = Students.objects.all()  # Get all Student records from the database
    serializer_class = StudentSerializer  # Use StudentSerializer to convert data to/from JSON

    # Handle GET request: return list of all employees
    def get(self, request):
        return self.list(request)  # Uses ListModelMixin’s built-in list() method
    
    # Handle POST request: create a new student
    def post(self, request):
        return self.create(request)  # Uses CreateModelMixin’s built-in create() method
    
class StudentDetail(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView,mixins.DestroyModelMixin, mixins.UpdateModelMixin,):
    queryset = Students.objects.all()  # Get all Employee records from the database
    serializer_class = StudentSerializer  # Use EmployeeSerializer to convert data to/from JSON

    # Handle GET request: return list of all employees
    def get(self, request, pk):
        return self.list(request, pk)  # Uses ListModelMixin’s built-in list() method
    
    # Handle POST request: create a new employee
    def put(self, request, pk):
        return self.update(request, pk)
    
    def delete(self, request, pk):
        return self.destroy(request, pk)