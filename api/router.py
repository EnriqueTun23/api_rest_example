from .viewsets import TodoViewSet
from rest_framework import routers

router = routers.DefaultRouter()

router.register('todos', TodoViewSet, base_name="todo")

# for url in router.urls:
#     print(url, '\n')