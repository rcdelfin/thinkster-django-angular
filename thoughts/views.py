from rest_framework import generics, permissions

from authentication.models import UserProfile
from thoughts.models import Thought
from thoughts.permissions import IsAuthenticatedAndOwnsObject
from thoughts.serializers import ThoughtSerializer


class ThoughtListCreateView(generics.ListCreateAPIView):
    queryset = Thought.objects.order_by('-created_at')
    serializer_class = ThoughtSerializer

    def get_permissions(self):
        if self.request.method == 'POST':
            return (permissions.IsAuthenticated(),)
        return (permissions.AllowAny(),)

    def pre_save(self, obj):
        obj.author = UserProfile.objects.get(user=self.request.user)
        return super(ThoughtListCreateView, self).pre_save(obj)


class ThoughtRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Thought.objects.all()
    serializer_class = ThoughtSerializer

    def get_permissions(self):
        if self.request.method not in permissions.SAFE_METHODS:
            return (IsAuthenticatedAndOwnsObject(),)
        return (permissions.AllowAny(),)
