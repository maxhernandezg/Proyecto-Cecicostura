from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from .models import Cart, ServiceHasCart
from services.models import Service

@login_required
def carrito(request):
    cart, created = Cart.objects.get_or_create(user=request.user)
    cart_items = ServiceHasCart.objects.filter(cart=cart)
    subtotal = sum(item.service.price * item.quantity for item in cart_items)
    total_normal = subtotal
    
    context = {
        'cart_items': cart_items,
        'subtotal': subtotal,
        'total_normal': total_normal,
    }

    return render(request, 'cart/carrito.html', context)

@login_required
def add_to_cart(request, service_id):
    service = get_object_or_404(Service, id=service_id)
    cart, created = Cart.objects.get_or_create(user=request.user)
    service_cart, created = ServiceHasCart.objects.get_or_create(cart=cart, service=service)
    if created:
        service_cart.quantity = 1  # Asigna el valor por defecto de 1
    else:
        service_cart.quantity += 1  # Incrementa la cantidad en 1 si ya existe en el carrito
    service_cart.save()
    return redirect('carrito')

@login_required
def remove_from_cart(request, service_id):
    service = get_object_or_404(Service, id=service_id)
    cart = get_object_or_404(Cart, user=request.user)
    cart_item = get_object_or_404(ServiceHasCart, cart=cart, service=service)
    
    if cart_item.quantity > 1:
        cart_item.quantity -= 1
        cart_item.save()
    else:
        cart_item.delete()

    return redirect('carrito')

@login_required
def whatsapp_checkout(request):
    cart = Cart.objects.get(user=request.user)
    message = cart.generate_whatsapp_message()
    whatsapp_url = f"https://wa.me/56987795611?text={message}"
    return redirect(whatsapp_url)
