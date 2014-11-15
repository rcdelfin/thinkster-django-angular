import json

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

from rest_framework import generics, permissions, status, views
from rest_framework.response import Response

from authentication.permissions import IsAuthenticatedAndOwnsProfile
from authentication.models import UserProfile
from authentication.serializers import UserProfileSerializer, UserSerializer

class UserCreateView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class LoginView(views.APIView):
    def post(self, request, format=None):
        data = json.loads(request.body)

        username = data.get('username', None)
        password = data.get('password', None)

        user = authenticate(username=username, password=password)

        if user is not None:
            if user.is_active:
                login(request, user)

                serialized = UserSerializer(user)

                return Response(serialized.data)
            else:
                return Response({
                    'error': 'Awkward! Your account has been disabled.'
                }, status=status.HTTP_401_UNAUTHORIZED)
        else:
            return Response({
                'error': 'Looks like your username or password is wrong. :('
            }, status=status.HTTP_400_BAD_REQUEST)


class LogoutView(views.APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request, format=None):
        logout(request)

        return Response({ 'success': True })


class UserProfileRetrieveUpdateView(generics.RetrieveUpdateAPIView):
    lookup_field = 'user__username'
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer

    def get_permissions(self):
        if self.request.method in permissions.SAFE_METHODS:
            return (permissions.AllowAny(),)
        return (IsAuthenticatedAndOwnsProfile(),)


class UserDestroyView(generics.DestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
