from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import status
from django.http import Http404
from rest_framework.response import Response
from .models import Phone, PhoneAllocate
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from .serializers import PhoneSerializer,PhoneAllocateCreateSerializer,PhoneAllocateUpdateSerializer,PhoneAllocateListSerializer
# Create your views here.

class PhoneList(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    def get_object(self, id):
        try:
            return Phone.objects.get(id=id)
        except Phone.DoesNotExist:
            raise Http404
    def post(self, request,format=None):
        serializer = PhoneSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    def get(self, request, id=None):
        if id:
            query = self.get_object(id)
            serializer = PhoneSerializer(query)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            query = Phone.objects.all()
            serializer = PhoneSerializer(query,many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        
    def put(self, request, id, format=None):
        try:
            get_phone = self.get_object(id)
            serializer = PhoneSerializer(get_phone, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors,status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)
    
    def delete(self, request, id):
        get_phone = self.get_object(id)
        get_phone.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class PhoneAllicationList(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    def post(self, request,format=None):
        serializer = PhoneAllocateCreateSerializer(data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    #show company's allocated device informations
    def get(self,request,id):
        allocated_device_info = PhoneAllocate.objects.filter(company=id)
        serializer = PhoneAllocateListSerializer(allocated_device_info,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    def put(self,request, id, format=None):
        try:
            allocate = PhoneAllocate.objects.get(id=id)
            print(allocate,id)
            serializer = PhoneAllocateUpdateSerializer(allocate, data= request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors,status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
    def delete(self, request, id, format=None):
        allocate = PhoneAllocate.objects.get(id=id)
        allocate.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
        
        

    