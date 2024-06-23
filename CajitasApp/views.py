from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm, UserChangeForm, UserCreationForm
from django.contrib.auth.decorators import login_required
from .forms import *
# Create your views here.

def inicio(req):
    return render(req, 'inicio.html', {})

   
def register(req):
    if req.method=='POST':
        miFormulario=UserCreationForm(req.POST)
        if miFormulario.is_valid():
            data=miFormulario.cleaned_data

            usuario = data["username"]
            miFormulario.save()
            
            return render(req, "inicio.html",{"message":f"Usuario {usuario} creado con éxito!"})

        else:
            return render(req, "inicio.html", {"message":"Datos invalidos."})     
    else:
        miFormulario=UserCreationForm()
        return render(req, "registro.html",{'miFormulario':miFormulario}) 
     
@login_required    
def editar_perfil(req):
    usuario= req.user
    if req.method=='POST':

        miFormulario=UserEditForm(req.POST, instance=req.user)

        if miFormulario.is_valid():

            data=miFormulario.cleaned_data

            usuario.first_name=data["first_name"]
            usuario.last_name=data["last_name"]
            usuario.email=data["email"]
            usuario.set_password(data["password1"])

            usuario.save()
        
            return render(req, "inicio.html",{"message":"Datos actualizados con exito."}) 
        else:
            return render(req, "editar_perfil.html", {'miFormulario':miFormulario})     
    else:
        miFormulario=UserEditForm(instance=req.user)

        return render(req, "editar_perfil.html",{'miFormulario':miFormulario})
