from rest_framework import serializers
from .models import Companyinfo
from Auth.serializers import UserListSerializer

class CompanyCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Companyinfo
        fields = ['user','company_name']
        
class CompanyShowSerializer(serializers.ModelSerializer):
    user = UserListSerializer()
    class Meta:
        model = Companyinfo
        fields = ['user','company_name']
        
