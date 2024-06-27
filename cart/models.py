from django.db import models
from django.contrib.auth.models import User
from services.models import Service

class Cart(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Cart {self.id} for {self.user}"
    
    def generate_whatsapp_message(self):
        items = ServiceHasCart.objects.filter(cart=self)
        message = "Hola, me gustaría comprar los siguientes productos:\n\n"
        for item in items:
            message += f"Producto: {item.service.title}\nCantidad: {item.quantity}\nPrecio: ${item.service.price * item.quantity}\n\n"
        total = sum(item.service.price * item.quantity for item in items)
        message += f"Total: ${total}"
        return message

class ServiceHasCart(models.Model):
    id = models.AutoField(primary_key=True)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)  # Valor por defecto
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('service', 'cart')

    def __str__(self):
        return f"{self.service} in cart {self.cart}"
