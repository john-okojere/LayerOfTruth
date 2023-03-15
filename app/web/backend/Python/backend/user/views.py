from django.shortcuts import render, redirect
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import UserSerializer,  RegisterSerializer
from django.contrib.auth import login, authenticate
from .models import User
from .forms import RegisterForm
from rest_framework.authentication import TokenAuthentication
from rest_framework import generics


from django.contrib.auth import get_user_model
User = get_user_model()

class UserDetailAPI(APIView):
    permission_classes = (AllowAny,)
    def get(self, request, *args, **kwargs):
        user = User.objects.get(id=request.user.id)
        serializer = UserSerializer(user)
        return Response(serializer.data)

class RegisterUserAPIView(generics.CreateAPIView):
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer


def homepage(request):
    return render(request, 'home/index.html')


def signup(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/')
    else:
        form = RegisterForm()
    return render(request, 'account/form.html', {'form': form})

