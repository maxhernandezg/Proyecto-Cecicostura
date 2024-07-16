from django.urls import path
from . import views

# Definición de las rutas URL para las vistas del carrito
urlpatterns = [
    # Ruta para ver el carrito de compras
    path('carrito/', views.carrito, name='carrito'),

    # Ruta para agregar un servicio al carrito
    path('add_to_cart/<int:service_id>/', views.add_to_cart, name='add_to_cart'),

    # Ruta para eliminar un servicio del carrito
    path('remove_from_cart/<int:service_id>/', views.remove_from_cart, name='remove_from_cart'),

    # Ruta para proceder al pago vía WhatsApp
    path('whatsapp_checkout/', views.whatsapp_checkout, name='whatsapp_checkout'),
]
