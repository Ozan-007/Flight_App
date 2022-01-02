from django.shortcuts import render
from rest_framework import generics,permissions
from accounts.models import Account

from accounts.serializers import AccountSerializer
# Create your views here.

class ListCreateAccountView(generics.ListCreateAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
    permission_classes = [permissions.IsAuthenticated]



class RetrieveUpdateDestroyAccountView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
    permission_classes = [permissions.IsAdminUser]
    

