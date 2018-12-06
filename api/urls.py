from django.urls import path, include
# from . import views
from .router import router

urlpatterns = [
    path('', include(router.urls)),
    # path('<int:pk>/', views.DetailTodo.as_view()),
    # path('rest-auth/', include('rest_auth.urls')),
]