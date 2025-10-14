from django.urls import path
from api.views import function_based_view

urlpatterns = [
    path('fbv-students/', function_based_view.studentView)
]