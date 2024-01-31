from django.shortcuts import render
from rest_framework import generics, permissions, status, views
from .serializers import *
from rest_framework.response import Response
from .utils import send_email_verification
from .models import *
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView


class CreateUserView(views.APIView):
    
    def post(self,request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            # print("serialier>",serializer)
            
            serializer.save()
            send_email_verification(serializer.data['email'], serializer.instance)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        

class VerifyEmail(views.APIView):
    def post(self, request):
        serializer = EmailVerificationSerializer(data=request.data)
        print(request.data)
        if serializer.is_valid(raise_exception=True):
            data = serializer.validated_data
            otp = data['token']
            user = User.objects.filter(email=data['email'])
            if not  user.exists():
                return Response({'error': 'Invalid credentials'}, status=status.HTTP_400_BAD_REQUEST)

            if user[0].otp != otp:
                return Response({'error': 'Invalid OTP'}, status=status.HTTP_400_BAD_REQUEST)
            user = user[0]
            user.is_verified = True
            user.save()
            if not Profile.objects.filter(user=user).exists():
                Profile.objects.create(user=user).save()
            
            print(user.is_verified)
        return Response({'email': 'Successfully activated'}, status=status.HTTP_200_OK)
    




# check if username is available

class CheckUsername(views.APIView):
    
    def post(self, request):
        username = request.data['username']
        if User.objects.filter(username=username).exists():
            return Response({'username_error': 'Username is already taken'}, status=status.HTTP_400_BAD_REQUEST)
        if not str(username).isalnum():
            # formate of alphanumeric is john123
            # alphanumerics that are not alphanumeric are john@123, john_123, john-123, john 123
            return Response({'username_error': 'The username should only contain alphanumeric characters'}, status=status.HTTP_400_BAD_REQUEST)
        return Response({'username': 'Username is available'}, status=status.HTTP_200_OK)

      
class CheckEmail(views.APIView):
    def post(self, request):
        email = request.data['email']
        if User.objects.filter(email=email).exists():
            return Response({'email_error': 'Email is already taken'}, status=status.HTTP_400_BAD_REQUEST)
        if not "@" in email:
            return Response({'email_error': 'Email is invalid'}, status=status.HTTP_400_BAD_REQUEST)
        return Response({'email': 'Email is Ok'}, status=status.HTTP_200_OK)

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer
    