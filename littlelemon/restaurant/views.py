from django.shortcuts import render
from rest_framework import generics, viewsets, permissions
from django.contrib.auth.models import User
from .models import Menu, Booking
from .serializers import MenuSerializer, BookingSerializer, UserSerializer

# Página principal
def index(request):
    return render(request, 'index.html', {})

# ✅ Vista para listar y crear ítems del menú (requiere autenticación)
class MenuListView(generics.ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    permission_classes = [permissions.IsAuthenticated]  # ✅ Todas las operaciones requieren autenticación

# ✅ Vista para obtener, actualizar y eliminar un ítem específico del menú
class MenuDetailView(generics.RetrieveUpdateDestroyAPIView):  # ✅ Permite DELETE
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    permission_classes = [permissions.IsAuthenticated]  # ✅ Solo usuarios autenticados

# ✅ Booking ViewSet (para reservas, requiere autenticación)
class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [permissions.IsAuthenticated]  # ✅ Requiere autenticación

# ✅ User ViewSet (para manejar usuarios, requiere autenticación)
class UserViewSet(viewsets.ModelViewSet):
   queryset = User.objects.all()
   serializer_class = UserSerializer
   permission_classes = [permissions.IsAuthenticated]  # ✅ Requiere autenticación