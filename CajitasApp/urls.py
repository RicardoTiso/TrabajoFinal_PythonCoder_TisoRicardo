from django.urls import path
from CajitasApp.views import *

urlpatterns = [
    path('', inicio, name='Inicio'),
    # path('login',login_view, name='Login'),
    path('registro',register, name='Registrar'),
    # path('logout', LogoutView.as_view(template_name="logout.html"), name='Logout'),
    path('editar-perfil', editar_perfil, name='EditaPerfil'),
    # path('agregar-avatar', agregar_avatar, name='AgregarAvatar'),
]
