from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from restaurant import views

# Router para ViewSets
router = routers.DefaultRouter()
router.register(r'booking', views.BookingViewSet)  # Rutas CRUD para reservas
router.register(r'users', views.UserViewSet)  # Rutas CRUD para usuarios

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # Incluir las rutas de la aplicación 'restaurant'
    path('restaurant/', include('restaurant.urls')),  # Incluye las URLs de la app "restaurant"
    
    # API con autenticación usando Bearer Token
    path('api/', include(router.urls)), 
    path('auth/', include('djoser.urls')),  
    path('auth/', include('djoser.urls.authtoken')),  
]