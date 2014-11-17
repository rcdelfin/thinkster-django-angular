from rest_framework import serializers

from authentication.models import Account


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ('id', 'email', 'username', 'created_at', 'updated_at',
                  'first_name', 'last_name', 'tagline',)
        read_only_fields = ('created_at', 'updated_at',)

    def restore_object(self, attrs, instance=None):
        if instance is not None:
            instance.tagline = attrs.get('tagline', instance.tagline)

            password = attrs.get('password', None)

            if password:
                instance.set_password(password)

            return instance
        return Account(**attrs)
