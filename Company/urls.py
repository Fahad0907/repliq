from django.urls import path,include
from .views import CompanyList
urlpatterns = [
    path('',CompanyList.as_view(),name="company")
    
]
