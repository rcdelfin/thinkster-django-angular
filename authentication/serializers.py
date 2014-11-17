from rest_framework import serializers

from authentication.models import Account


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ('id', 'email', 'password', 'created_at', 'updated_at',
                  'first_name', 'last_name', 'tagline',)
        read_only_fields = ('created_at', 'updated_at',)
        write_only_fields = ('password',)

    def restore_object(self, attrs, instance=None):
        account = super(AccountSerializer, self).restore_object(attrs, instance)
        password = attrs.get('password', None)

        if password:
            account.set_password(password)

        return account
