from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import TeacherSerializer, StudentSerializer, GroupsSerializer, ParentsSerializer, LoginSerializer
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .models import Teacher
from rest_framework_simplejwt.tokens import AccessToken, RefreshToken
# Create your views here.

class RegisterStudentApi(APIView):
    
    def post(request):
        serializer = StudentSerializer(request.data)
        
        if serializer.is_valid():
            
            serializer.save()
            
            return Response({"msg":"User Created"}, status=201)
        else:
            return Response(serializer.errors)


class RegisterTeacherApi(APIView):
    
    def post(request):
        import random
        name = request.data.get("name")
        phone = request.data.get("phone")
        password = request.data.get("password")
        role = request.data.get("role")
        branch = request.data.get("branch")
        modme_id = random.randint(10000, 99999)
        try:
            data = Teacher.objects.create(name = name,modme_id = modme_id,phone = phone, password = password, role = role, branch = branch)
            data.save()
            return Response({"msg":"User Created"}, status=201)
        except:
            return Response({"msg": "User not created !"})
        
        

class RegisterParentApi(APIView):
    
    def post(request):
        serializer = ParentsSerializer(request.data)
        
        if serializer.is_valid():
            
            serializer.save()
            
            return Response({"msg":"User Created"}, status=201)
        else:
            return Response(serializer.errors)



        
class RegisterGroupApi(APIView):
    
    def post(request):
        serializer = GroupsSerializer(request.data)
        
        if serializer.is_valid():
            
            serializer.save()
            
            return Response({"msg":"Group Created"}, status=201)
        else:
            return Response(serializer.errors)

        
        
class LoginApi(TokenObtainPairView):
    serializer_class = LoginSerializer
            