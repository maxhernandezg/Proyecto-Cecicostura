from django.urls import path
from .views import CustomLoginView, CustomSignUpView

urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('signup/', CustomSignUpView.as_view(), name='signup'),
]
