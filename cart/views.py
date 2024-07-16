from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from .models import Cart, ServiceHasCart
from services.models import Service

# Vista para mostrar el carrito de compras
@login_required
def carrito(request):
    # Obtiene o crea un carrito para el usuario autenticado
    cart, created = Cart.objects.get_or_create(user=request.user)

    # Obtiene los elementos del carrito
    cart_items = ServiceHasCart.objects.filter(cart=cart)

    # Calcula el subtotal del carrito
    subtotal = sum(item.service.price * item.quantity for item in cart_items)

    # Asigna el subtotal al total normal (se puede modificar según las necesidades)
    total_normal = subtotal

    # Contexto a pasar a la plantilla
    context = {
        'cart_items': cart_items,
        'subtotal': subtotal,
        'total_normal': total_normal,
    }

    # Renderiza la plantilla del carrito con el contexto
    return render(request, 'cart/carrito.html', context)

# Vista para agregar un servicio al carrito
@login_required
def add_to_cart(request, service_id):
    # Obtiene el servicio por su ID o lanza un error 404 si no existe
    service = get_object_or_404(Service, id=service_id)

    # Obtiene o crea un carrito para el usuario autenticado
    cart, created = Cart.objects.get_or_create(user=request.user)

    # Obtiene o crea un elemento del carrito que relaciona el servicio con el carrito
    service_cart, created = ServiceHasCart.objects.get_or_create(cart=cart, service=service)

    # Si se creó un nuevo elemento del carrito, asigna una cantidad por defecto de 1
    if created:
        service_cart.quantity = 1
    else:
        # Si ya existe, incrementa la cantidad en 1
        service_cart.quantity += 1

    # Guarda el elemento del carrito
    service_cart.save()

    # Redirige a la vista del carrito
    return redirect('carrito')

# Vista para eliminar un servicio del carrito
@login_required
def remove_from_cart(request, service_id):
    # Obtiene el servicio por su ID o lanza un error 404 si no existe
    service = get_object_or_404(Service, id=service_id)

    # Obtiene el carrito del usuario autenticado o lanza un error 404 si no existe
    cart = get_object_or_404(Cart, user=request.user)

    # Obtiene el elemento del carrito que relaciona el servicio con el carrito o lanza un error 404 si no existe
    cart_item = get_object_or_404(ServiceHasCart, cart=cart, service=service)

    # Si la cantidad del elemento es mayor que 1, la reduce en 1
    if cart_item.quantity > 1:
        cart_item.quantity -= 1
        cart_item.save()
    else:
        # Si la cantidad es 1 o menor, elimina el elemento del carrito
        cart_item.delete()

    # Redirige a la vista del carrito
    return redirect('carrito')

# Vista para proceder al pago vía WhatsApp
@login_required
def whatsapp_checkout(request):
    # Obtiene el carrito del usuario autenticado
    cart = Cart.objects.get(user=request.user)

    # Genera el mensaje para WhatsApp con los detalles del carrito
    message = cart.generate_whatsapp_message()

    # URL para redirigir a WhatsApp con el mensaje predefinido
    whatsapp_url = f"https://wa.me/56987795611?text={message}"

    # Redirige a la URL de WhatsApp
    return redirect(whatsapp_url)
