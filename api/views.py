from django.shortcuts import render

# Create your views here.
from rest_framework import generics, viewsets
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from todos import models
from . import serializers

# class ListTodo(generics.ListCreateAPIView):
#     queryset = models.Todos.objects.all()
#     serializer_class = serializers.TodoSerializer
# class ListTodo(generics.ListAPIView):
class ListTodo(viewsets.ModelViewSet):
    queryset = models.Todos.objects.all()
    serializer_class = serializers.TodoSerializer
    # authentication_classes = (TokenAuthentication)
    # permission_classes = [IsAuthenticated]

class DetailTodo(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Todos.objects.all()
    serializer_class = serializers.TodoSerializer