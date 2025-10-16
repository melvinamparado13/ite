from django.urls import path
from api.views import function_based_view

urlpatterns = [
    path('fbv-students/', function_based_view.studentView),
    path('fbv-student/<int:student_id>', function_based_view.student)
]