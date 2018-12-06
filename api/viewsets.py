from todos.models import Todos
from .serializers import TodoSerializer
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
# class TodoViewSet(viewsets.ViewSet):

#     def list(self, request):
#         queryset = Todos.objects.all()
#         serializer = TodoSerializer(queryset, many=True)
#         return Response(serializer.data)



class TodoViewSet(viewsets.ModelViewSet):
    queryset = Todos.objects.all()
    serializer_class = TodoSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    @action(methods=['get'], detail=False)
    def newest(self, request):
        newest = self.get_queryset().order_by('fecha_de_registro').last()
        serializer =  self.get_serializer_class()(newest)
        return Response(serializer.data)