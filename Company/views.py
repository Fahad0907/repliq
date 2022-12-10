from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Companyinfo
from .serializers import CompanyCreateSerializer,CompanyShowSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
# Create your views here.

class CompanyList(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    def post(self,request,format = None):
        serializer = CompanyCreateSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    def get(self, request):
        query = Companyinfo.objects.all()
        print(query)
        serializer = CompanyShowSerializer(query,many=True)
        return Response(serializer.data)
       