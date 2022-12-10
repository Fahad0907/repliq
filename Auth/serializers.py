from rest_framework import serializers
from .models import UserAccount

class UserRegistrationSerializer(serializers.ModelSerializer):
    re_password = serializers.CharField(
        write_only=True,
        required=True,
    )
    class Meta:
        model = UserAccount
        fields = ['email','username','password','re_password','phone']
        extra_kwargs = {'password' : {'write_only' : True}}
    def validate(self, attrs):
        password = attrs.get('password')
        re_password = attrs.get('re_password')
        if password != re_password:
            raise serializers.ValidationError('Passwords did not match')
        attrs.pop('re_password')
        return attrs
    def create(self, validate_data):
        return UserAccount.objects.create_user(**validate_data)
    
class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAccount
        fields = ['id','username','email','is_superuser','isEmploye','phone']