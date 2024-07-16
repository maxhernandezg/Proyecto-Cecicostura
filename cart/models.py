from django.db import models
from django.contrib.auth.models import User
from services.models import Service

class Cart(models.Model):
    """
    Modelo que representa un carrito de compras.
    """

    # Campo que representa el ID del carrito
    id = models.AutoField(primary_key=True)

    # Relación uno a uno con el modelo User. Cada usuario tiene un carrito único.
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    # Campos para almacenar la fecha y hora de creación y actualización del carrito.
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        """
        Método mágico para representar el carrito como una cadena.
        """
        return f"Cart {self.id} for {self.user}"
    
    def generate_whatsapp_message(self):
        """
        Genera un mensaje para enviar por WhatsApp con los detalles del carrito.
        """
        # Obtiene todos los elementos del carrito asociados a este carrito
        items = ServiceHasCart.objects.filter(cart=self)

        # Inicializa el mensaje con un saludo
        message = "Hola, me gustaría contratar los siguientes servicios:\n\n"

        # Itera sobre cada elemento del carrito y añade detalles al mensaje
        for item in items:
            message += f"Servicio: {item.service.title}\nCantidad: {item.quantity}\nPrecio: ${item.service.price * item.quantity}\n\n"

        # Calcula el total de la compra
        total = sum(item.service.price * item.quantity for item in items)

        # Añade el total al mensaje
        message += f"Total: ${total}"

        # Devuelve el mensaje generado
        return message


class ServiceHasCart(models.Model):
    """
    Modelo que representa la relación entre un servicio y un carrito de compras.
    """

    # Campo que representa el ID de la relación
    id = models.AutoField(primary_key=True)

    # Relación muchos a uno con el modelo Service. Un servicio puede estar en muchos carritos.
    service = models.ForeignKey(Service, on_delete=models.CASCADE)

    # Relación muchos a uno con el modelo Cart. Un carrito puede tener muchos servicios.
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)

    # Campo para almacenar la cantidad del servicio en el carrito. Valor por defecto de 1.
    quantity = models.PositiveIntegerField(default=1)

    # Campos para almacenar la fecha y hora de creación y actualización de la relación.
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)

    class Meta:
        """
        Metadatos para el modelo ServiceHasCart.
        """
        # Define que la combinación de 'service' y 'cart' debe ser única.
        unique_together = ('service', 'cart')

    def __str__(self):
        """
        Método mágico para representar la relación como una cadena.
        """
        return f"{self.service} in cart {self.cart}"
