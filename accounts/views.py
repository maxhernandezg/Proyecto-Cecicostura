from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.shortcuts import redirect

# Define una clase CustomLoginView que extiende LoginView
class CustomLoginView(LoginView):
    
    # Sobrescribe el método dispatch para agregar lógica personalizada
    def dispatch(self, request, *args, **kwargs):
        # Verifica si el usuario ya está autenticado
        if request.user.is_authenticated:
            # Si el usuario está autenticado, redirige a la página de inicio (index)
            return redirect('index')
        # Si el usuario no está autenticado, continúa con el comportamiento estándar de LoginView
        return super().dispatch(request, *args, **kwargs)
    
class CustomSignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('index')  # Redirige al index si el usuario está autenticado
        return super().dispatch(request, *args, **kwargs)