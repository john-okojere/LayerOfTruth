from rest_framework import serializers, status
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password

#Serializer to get Detail using Django Token Authentication
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        field = ['id', 'first_name', 'last_name', 'username']

class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True,
        validators = [UniqueValidator(queryset=User.objects.all())])
    password = serializers.CharField(write_only=True, validators=[validate_password])
    password = serializers.CharField(write_only=True, require=True)
    class Meta:
        model = User
        fields = ('username', 'password', 'email', 'first_name', 'last_name')
        extra_kwargs = {
            'first_name':{'required':True},
            'last_name': {'require':True}
        }
    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError(
                {'Password':"Password field didn't match"}
            )
        return attrs
    def create(self, validated_data):
        user = User.objects.create(
            username = validated_data['username'],
            email = validated_data['email'],
            first_name = validated_data['first_name'],
            last_name = validated_data['last_name']
        )
        user.set_password(validated_data['password'])
        user.save()        
        return user