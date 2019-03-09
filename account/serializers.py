from rest_framework import serializers

from .models import *


class AccountTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = AccountType
        fields = ("id", "description", "tax_rate", "is_active", )


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ("id", "account", "last_name", "first_name", "email", "primary_phone", "alternate_phone", "fax",
                  "do_notify", "notes", )


class AccountSerializer(serializers.ModelSerializer):
    account_type = AccountTypeSerializer()
    contacts = ContactSerializer(many=True)

    class Meta:
        model = Account
        fields = ("id", "account_type", "account_number", "name", "address", "city", "state", "zip", "notes",
                  "contacts", )
