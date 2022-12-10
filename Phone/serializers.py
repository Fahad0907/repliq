from rest_framework import serializers
from .models import Phone, PhoneAllocate
from Auth.serializers import UserListSerializer
from Company.serializers import CompanyShowSerializer

class PhoneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Phone
        fields = ['id','device_name','device_condition']
        extra_kwargs = {'id': {'read_only': True}}
        
        
class PhoneAllocateCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = PhoneAllocate
        fields = ['id','device','user','company']
        extra_kwargs = {'id': {'read_only': True}}

class PhoneAllocateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = PhoneAllocate
        fields = ['id','device','user','company','received_time','received_condition','provide_time']
        extra_kwargs = {'id': {'read_only': True}}
    
class PhoneAllocateListSerializer(serializers.ModelSerializer):
    user = UserListSerializer()
    company = CompanyShowSerializer()
    class Meta:
        model = PhoneAllocate
        fields = ['id','device','user','company','provide_time','received_time','received_condition']
        extra_kwargs = {'id': {'read_only': True}}
        
    