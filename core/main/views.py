from django.shortcuts import render
from .serializers import PhoneSerializer
from rest_framework import viewsets
from .models import Phone
# Create your views here.

class PhoneViewSet(viewsets.ModelViewSet):
    queryset = Phone.objects.all()
    serializer_class = PhoneSerializer