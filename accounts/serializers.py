from rest_framework import serializers
from .models import User
from django.contrib.auth.models import Group
from api.serializers import *
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken



def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)

    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }



class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=10, write_only=True)
    class Meta:
        model = User
        fields = ['name', 'email', 'password']

    
    def create(self, validated_data):
        user = User.objects.create_user(
            name = validated_data['name'],
            email = validated_data['email'],
            role = validated_data['role'],
            password = validated_data['password']
        )
        user.save()
        if validated_data['role'] == 'D' or validated_data['role'] == 'doctor':
            group = Group.objects.get(name='Doctors')

        else:
            group = Group.objects.get(name='Patients')
        user.groups.add(group)
        return user
    

class LogInSerializer(serializers.ModelSerializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['email', 'password']

    
    def validate(self, validated_data):
        email = validated_data['email']
        if not User.objects.filter(email=email).exists():
            raise serializers.ValidationError("user doesn't exists")
        
        auth_user = authenticate(email=email, password=validated_data['password'])
        if not auth_user:
            raise serializers.ValidationError('Invalid credentials!')
        data = get_tokens_for_user(auth_user)

        return data