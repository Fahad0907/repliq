from django.shortcuts import render
from .serializers import UserRegistrationSerializer,UserListSerializer
from .models import UserAccount
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib import auth
from rest_framework_simplejwt.tokens import RefreshToken
# Create your views here.
class UserRegisterView(APIView):
    def post(self, request,format=None):
        serializer = UserRegistrationSerializer(data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def get(self,request):
        query= UserAccount.objects.all()
        serializer = UserListSerializer(query,many=True)
        return Response(serializer.data)

class Login(APIView):
    def post(self, request):
        print('found')
        email = request.data['email']
        password = request.data['password']
        user = auth.authenticate(email=email, password=password)
        print(user)
        if user is not None:
            auth.login(request, user)
            refresh = RefreshToken.for_user(user)
            return Response({
                "status" : status.HTTP_200_OK,
                'refresh': str(refresh),
                'access': str(refresh.access_token)}
            )
            
        else:
            return Response({"status" : status.HTTP_401_UNAUTHORIZED})