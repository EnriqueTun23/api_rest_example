from django.urls import path, include
# from . import views
from .router import router
from .views import (ListTodoAPI, DetailTodoAPI, 
CreateTodoAPI, UpadateTodoAPI, DeleteTodpAPI)

urlpatterns = [
    path('', include(router.urls)),
    # path('<int:pk>/', views.DetailTodo.as_view()),
    # path('rest-auth/', include('rest_auth.urls')),
    path('ejemplo/', ListTodoAPI.as_view()),
    path('ejemplo/<int:pk>/', DetailTodoAPI.as_view(), name="detail"),
    path('ejemplo/create/', CreateTodoAPI.as_view(), name="create"),
    path('ejemplo/<int:pk>/edit', UpadateTodoAPI.as_view(), name="update"),
    path('ejemplo/<int:pk>/delete', DeleteTodpAPI.as_view())
]