from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
from .serializers import UserSerializer
from .models import Utilisateur,Participant,Woofer
from rest_framework.viewsets import ViewSet
from rest_framework.views import APIView
from rest_framework.decorators import action
from django.conf import settings
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken, AccessToken
from rest_framework.permissions import AllowAny, IsAuthenticated

# TOKEN_EXPIRATION_ACCESS = 600
# TOKEN_EXPIRATION_REFRESH = 1440

# Create your views here.

class RegisterView(APIView):
    permission_classes = [AllowAny]  # You can update this to any other permission later

    def post(self, request):
        user_type = request.data.get('user_type')
        
        
        if user_type not in ['Participant', 'Woofer']:
            return Response({'error': 'Invalid user type. Only "Participant" or "Woofer" allowed.'}, 
                            status=status.HTTP_403_FORBIDDEN)

        # Serialize the user data
        serializer = UserSerializer(data=request.data)
        
        if serializer.is_valid():
            user = serializer.save()  # Save the user instance
            
            # Create the corresponding class instance based on user_type
            if user_type == 'Participant':
                Participant.objects.create(user=user)
            elif user_type == 'Woofer':
                Woofer.objects.create(user=user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)     
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class LoginView(APIView):
    permission_classes = [AllowAny]  # Allow access to anyone

    def post(self, request, *args, **kwargs):
        print(request.user.username)

        username = request.data.get('username')
        password = request.data.get('password')

        # Check if username and password are provided
        if not username or not password:
            raise AuthenticationFailed('Username and password are required.')

        user = Utilisateur.objects.filter(username=username).first()

        if user is None:
            raise AuthenticationFailed('User not found!')

        if not user.check_password(password):
            raise AuthenticationFailed('Incorrect password!')
        

        refresh = RefreshToken.for_user(user)
        access = refresh.access_token
        refresh_token = str(refresh)
        access_token = str(access)
        response = Response()

        # Set the RefreshToken cookie
        response.set_cookie(key='RefreshToken', value=refresh_token, httponly=True)

        # Return access token and user type in the response
        response.data = {
            'AccessToken': access_token,
            'user-type': user.user_type
        }

        return response  
 
class LogoutView(APIView):
    permission_classes = [IsAuthenticated]  # Ensure only authenticated users can log out

    def post(self, request, *args, **kwargs):
        response = Response()

        # Delete the RefreshToken cookie
        response.delete_cookie('RefreshToken')

        # Return a success message
        response.data = {
            'message': 'success'
        }

        return response       