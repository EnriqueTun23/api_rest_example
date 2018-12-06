from rest_framework import serializers
from todos import models

class TodoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Todos
        fields = ('id', 'primer_nombre', 'segundo_nombre', 
        'apellido_paterno', 'apellido_materno', 'email',
        'telefono')

        