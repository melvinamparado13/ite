from django.urls import path
from django.http import HttpResponse
from api.views import student_function_based_view
from api.views import employee_function_based_view
from api.views import student_class_based_view
from api.views import employee_class_based_view
from api.views import mixins_employee
from api.views import mixins_student
from api.views import generic_employee


urlpatterns = [
    path('fbv-students/', student_function_based_view.studentView),
    path('fbv-student/<int:student_id>', student_function_based_view.student),

    path('fbv-employees/', employee_function_based_view.employeeView),
    path('fbv-employee/<int:employee_id>/', employee_function_based_view.employee),

    path('cbv-students/', student_class_based_view.Student.as_view()),
    path('cbv-student/<int:pk>/', student_class_based_view.StudentDetail.as_view()),

    path('cbv-employees/', employee_class_based_view.Employees.as_view()),
    path('cbv-employee/<int:pk>/', employee_class_based_view.EmployeeDetail.as_view()),

    path('mixins-employees/', mixins_employee.Employees.as_view()),
    path('mixins-employee-detail/<int:pk>/', mixins_employee.EmployeeDetail.as_view()),

    path('mixins-students/', mixins_student.Student.as_view()),
    path('mixins-student-detail/<int:pk>/', mixins_student.StudentDetail.as_view()),

    path('generic-employee/', generic_employee.Employees.as_view()),
    path('generic-employee-detail/<int:pk>/', generic_employee.EmployeeDetail.as_view()),
]