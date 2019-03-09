from rest_framework import viewsets

from .models import Account, AccountType, Contact
from .serializers import AccountSerializer, AccountTypeSerializer, ContactSerializer


class AccountTypeViewSet(viewsets.ModelViewSet):
    serializer_class = AccountTypeSerializer
    queryset = AccountType.objects.all()


class AccountViewSet(viewsets.ModelViewSet):
    serializer_class = AccountSerializer
    queryset = Account.objects.all()


class ContactViewSet(viewsets.ModelViewSet):
    serializer_class = ContactSerializer
    queryset = Contact.objects.all()
