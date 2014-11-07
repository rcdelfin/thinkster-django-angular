from rest_framework import serializers

from authentication.serializers import UserProfileSerializer
from thoughts.models import Thought


class ThoughtSerializer(serializers.ModelSerializer):
    author = UserProfileSerializer()

    class Meta:
        model = Thought

        fields = ('id', 'author', 'content', 'created_at', 'updated_at')
        read_only_fields = ('id', 'created_at', 'updated_at')
