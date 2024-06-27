from django.urls import path
from . import views

urlpatterns = [
    path('carrito/', views.carrito, name='carrito'),
    path('add_to_cart/<int:service_id>/', views.add_to_cart, name='add_to_cart'),
    path('remove_from_cart/<int:service_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('whatsapp_checkout/', views.whatsapp_checkout, name='whatsapp_checkout'),
]
