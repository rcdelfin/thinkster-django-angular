from rest_framework import permissions

from thoughts.models import Thought


class IsAuthenticatedAndOwnsObject(permissions.BasePermission):
    def has_permission(self, request, view):
        if not request.user.is_authenticated():
            return False

        _id = self.kwargs['pk']

        return Thought.objects.filter(id=_id, author_id=request.user).exists()
