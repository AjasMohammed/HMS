from rest_framework.response import Response
from .models import User
from rest_framework.views import APIView
from rest_framework import status
from .serializers import UserSerializer, LogInSerializer

from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import AllowAny, IsAuthenticated


class LoginUser(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [AllowAny]
    def post(self, request):
        
        serializer = LogInSerializer(data=request.data)
        if serializer.is_valid():
            data = serializer.validated_data
            return Response(data=data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            


class RegisterUser(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors)
        serializer.save()

        return Response({'message': 'User created successfully.'}, status=status.HTTP_201_CREATED)
    

class LogoutUser(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        refresh_token = request.data.get('refresh_token')
        if not refresh_token:
            return Response({"message": "refresh token is missing!"}, status=status.HTTP_400_BAD_REQUEST)
        try:
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response({'message': "Successfully LoggedOut!"})
        except:
            return Response({"message": "token is invalid!"}, status=status.HTTP_404_NOT_FOUND)