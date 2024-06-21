from django.urls import path
from . import views

urlpatterns = [
    path('', views.servicios, name='servicios'),
    path('<int:id>/', views.descripcion_servicio, name='descripcion_servicio'),
]
