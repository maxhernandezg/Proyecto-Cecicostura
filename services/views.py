from django.shortcuts import render

# Create your views here.
def servicios(request):
    return render(request, 'services/servicios.html')

def descripcion_servicio(request, id):
    return render(request, 'services/descripcion_servicio.html', {'id': id})