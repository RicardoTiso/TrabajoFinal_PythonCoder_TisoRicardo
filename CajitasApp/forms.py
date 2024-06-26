from typing import Any
from django import forms
from .models import Avatar
from django.contrib.auth.forms import  UserChangeForm 
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _ 

# class CursoFormulario(forms.Form):
#     curso=forms.CharField()
#     camada=forms.IntegerField()

# class CursoFormulario(forms.ModelForm):
#     class Meta:
#         model=Curso
#         fields=("__all__")

# class ProfesorFormulario(forms.Form):
#     nombre=forms.CharField()
#     apellido=forms.CharField()
#     email=forms.EmailField()
#     profesion=forms.CharField()

# forms.py



class UserEditForm(UserChangeForm):
    password= forms.CharField(
        help_text="",
        widget=forms.HiddenInput(),
        required=False
    )
    password1=forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2=forms.CharField(label="Repetir Contraseña", widget=forms.PasswordInput)
    class Meta:
        model=User
        fields=["first_name", "last_name", "email"]
        
    def clean_password2(self):
        password1 = self.cleaned_data["password1"]
        password2 = self.cleaned_data["password2"]

        if password1 != password2:
            raise forms.ValidationError("Las contraseñas no coinciden")
        return password2
    
class AvatarFormulario(forms.ModelForm):
    class Meta:
        model=Avatar
        fields=('imagen',)