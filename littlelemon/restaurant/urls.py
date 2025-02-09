from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('', views.index, name='index'),
    
    # ✅ Rutas para el menú
    path('menu/', views.MenuListView.as_view(), name='menu-list'),  # GET (listar), POST (crear)
    path('menu/<int:pk>/', views.MenuDetailView.as_view(), name='menu-detail'),  # ✅ GET, PUT, DELETE
    
    # ✅ Endpoint para obtener el token de autenticación
    path('api-token-auth/', obtain_auth_token, name='api-token-auth'),
]