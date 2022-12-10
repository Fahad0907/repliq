from rest_framework import serializers
from Auth.serializers import UserListSerializer
from Company.serializers import CompanyShowSerializer
from .models import EmployeeInfo

class EmployeeShowSerializer(serializers.ModelSerializer):
    employee_info = UserListSerializer()
    company_info = CompanyShowSerializer()
    class Meta:
        model = EmployeeInfo
        fields = ['employee_info','company_info']
        
class EmployeeCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployeeInfo
        fields= ['user','company']
    