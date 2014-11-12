from rest_framework import serializers

from authentication.serializers import UserProfileSerializer
from thoughts.models import Thought


class ThoughtSerializer(serializers.ModelSerializer):
    author = UserProfileSerializer(required=False)

    class Meta:
        model = Thought

        fields = ('id', 'author', 'content', 'created_at', 'updated_at')
        read_only_fields = ('id', 'created_at', 'updated_at')

    def get_validation_exclusions(self, *args, **kwargs):
        exclusions = super(ThoughtSerializer, self).get_validation_exclusions()

        return exclusions + ['author']


class AuthorlessThoughtSerializer(serializers.ModelField):
    class Meta:
        model = Thought

        fields = ('id', 'content', 'created_at', 'updated_at')
        read_only_fields = ('id', 'created_at', 'updated_at')
