from rest_framework.permissions import BasePermission



class IsOwnerOrReadOnly(BasePermission):
    message = "Hola creaa tu usuario o logeate para poder ver los datos"
    def has_object_permission(self, request, view, obj):
            return obj.user == request.user