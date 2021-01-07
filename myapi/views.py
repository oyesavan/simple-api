from django.shortcuts import render
from rest_framework import viewsets
from .serializers import HeroSerializer
from .models import Hero
from rest_framework import generics

class HeroViewSet(generics.ListCreateAPIView):
    queryset = Hero.objects.all().order_by('name')
    serializer_class = HeroSerializer



# Create your views here.
