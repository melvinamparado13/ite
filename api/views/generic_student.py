from rest_framework import generics
from students.models import Students
from api.serializer import StudentSerializer

# class Student(generics.ListAPIView, generics.CreateAPIView, ):
#     queryset = Students.objects.all()
#     serializer_class = StudentsSerializer

# Option 2
class Student(generics.ListCreateAPIView):
    queryset = Students.objects.all()
    serializer_class = StudentSerializer

# class StudentDetail(generics.RetrieveAPIView, generics.UpdateAPIView, generics.DestroyAPIView):
#     queryset = Students.objects.all()
#     serializer_class = StudentSerializer
#     Lookup_field = 'pk'

# Option 2
class StudentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Students.objects.all()
    serializer_class = StudentSerializer
    lookup_field = 'pk'