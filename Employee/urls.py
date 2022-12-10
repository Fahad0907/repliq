from django.urls import path,include
from .views import EmployeeList
urlpatterns = [
    path("info/",EmployeeList.as_view(),name="employeeinfo")
]
