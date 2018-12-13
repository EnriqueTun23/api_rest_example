from rest_framework import serializers
from todos import models

class TodoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Todos
        fields = ('id', 'primer_nombre', 'segundo_nombre', 
        'apellido_paterno', 'apellido_materno', 'email',
        'telefono')

class TodoCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Todos
        fields = ('primer_nombre', 'segundo_nombre','apellido_paterno', 'apellido_materno', 'email',
        'telefono')

class TodoDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Todos
        fields = ('id', 'primer_nombre', 'segundo_nombre', 
        'apellido_paterno', 'apellido_materno', 'email',
        'telefono', 'fecha_de_registro', 'fecha_de_actualizacion')

class TodoUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Todos
        fields = ('primer_nombre', 'segundo_nombre', 
        'apellido_paterno', 'apellido_materno', 'email',
        'telefono',)