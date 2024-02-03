from django.shortcuts import get_object_or_404
from rest_framework.serializers import Serializer, ModelSerializer
from rest_framework_simplejwt.serializers import (
    TokenObtainPairSerializer,
    TokenRefreshSerializer,
)
from rest_framework_simplejwt.tokens import AccessToken
from rest_framework.exceptions import ValidationError
from django.contrib.auth import authenticate
from .models import Student, Teacher, Parents, Groups



class TeacherSerializer(ModelSerializer):
    class Meta:
        model = Teacher
        fields = ("name","phone","password","role","branch")


class ParentsSerializer(ModelSerializer):
    class Meta:
        model = Parents
        fields = "__all__"
        

class GroupsSerializer(ModelSerializer):
    class Meta:
        model = Groups
        fields = "__all__"



class StudentSerializer(ModelSerializer):
    class Meta:
        model = Student
        fields = "__all__"
        
        
        
class LoginSerializer(TokenObtainPairSerializer):
    
    def validate(self, data):
        phone = data.get("phone")
        password = data.get("password")
        auth_kwarg = {self.username_field: phone, "password": password}
        user = authenticate(**auth_kwarg)
        if user is not None:
            self.user = user
        else:
            data = {
                "status" : "False",
                "msg" : "Login or password wrong"
            }
            raise ValidationError(data)
        data  = self.user.token()
        return data
    
    


        
            
