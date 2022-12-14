from django.shortcuts import render
from .serializers import PhoneSerializer, CategorySerializer
from rest_framework import viewsets
from .models import Phone, Category
# Create your views here.

class PhoneViewSet(viewsets.ModelViewSet):
    queryset = Phone.objects.all()
    serializer_class = PhoneSerializer

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer