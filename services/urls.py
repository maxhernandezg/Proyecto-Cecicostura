from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
    path('', views.servicios, name='servicios'),
    path('<int:id>/', views.descripcion_servicio, name='descripcion_servicio'),
]
