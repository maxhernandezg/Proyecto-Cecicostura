from django.shortcuts import render, get_object_or_404
from .models import Service

# Create your views here.
def servicios(request):
    servicios = Service.objects.all()
    context = {"servicios":servicios}

    return render(request, 'services/servicios.html', context)

def descripcion_servicio(request, id):
    servicio = get_object_or_404(Service, id=id) # Obtén el servicio o muestra un error 404 si no existe
    context =   {'servicio': servicio}
    return render(request, 'services/descripcion_servicio.html', context)