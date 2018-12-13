from django.shortcuts import render, get_object_or_404

# Create your views here.
from rest_framework import generics, viewsets
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from todos import models
from . import serializers
from .permissions import IsOwnerOrReadOnly
from .pagination import PostLimitOffsetPagination, PostPageNumberPagination
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

class ListTodoAPI(generics.ListAPIView):
    queryset = models.Todos.objects.all()
    serializer_class = serializers.TodoSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = [IsAuthenticated,]
    pagination_class = PostPageNumberPagination

class DetailTodoAPI(generics.RetrieveAPIView):
    queryset = models.Todos.objects.all()
    serializer_class = serializers.TodoDetailSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = [IsAuthenticated,]

    ''' Sirve para sacar un boton de delete y poder eliminar 
        con el peja ejemplo 0.0.0.0/data/1/delete '''
    def delete(self, request, pk):
        queryset = get_object_or_404(models.Todos, id=pk)
        queryset.delete()
    
class CreateTodoAPI(generics.CreateAPIView):
    queryset = models.Todos.objects.all()
    serializer_class = serializers.TodoCreateSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = [IsAuthenticated,]

    '''Sirve cuando quieres saber el user que creo el post'''
    # def perform_create(self, serializer):
    #     serializer.save(user=self.reques)

class UpadateTodoAPI(generics.RetrieveUpdateAPIView):
    queryset = models.Todos.objects.all()
    serializer_class = serializers.TodoUpdateSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = [IsAuthenticated]

class DeleteTodpAPI(generics.DestroyAPIView):
    queryset = models.Todos.objects.all()
    serializer_class = serializers.TodoDetailSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = [IsAuthenticated]