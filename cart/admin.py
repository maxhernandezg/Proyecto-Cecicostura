from django.contrib import admin
from .models import Cart, ServiceHasCart

# Registrando el modelo Cart en el admin de Django
admin.site.register(Cart)

# Registrando el modelo ServiceHasCart en el admin de Django
admin.site.register(ServiceHasCart)
