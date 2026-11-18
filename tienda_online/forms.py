from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Producto, Categoria


class RegistroUsuarioForm(UserCreationForm):
    """
    Formulario de registro de usuario con etiquetas y textos de ayuda en español.
    """
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'username' in self.fields:
            self.fields['username'].label = "Nombre de usuario"
            self.fields['username'].help_text = "Requerido. Máximo 150 caracteres. Solo letras, dígitos y @/./+/-/_."
            self.fields['username'].widget.attrs.update({
                'placeholder': 'Ingresa tu nombre de usuario...'
            })
        if 'password1' in self.fields:
            self.fields['password1'].label = "Contraseña"
            self.fields['password1'].help_text = "La contraseña debe tener al menos 8 caracteres y no ser común."
            self.fields['password1'].widget.attrs.update({
                'placeholder': '••••••••'
            })
        if 'password2' in self.fields:
            self.fields['password2'].label = "Confirmar contraseña"
            self.fields['password2'].help_text = "Ingresa nuevamente la misma contraseña para verificarla."
            self.fields['password2'].widget.attrs.update({
                'placeholder': '••••••••'
            })


class ProductoForm(forms.ModelForm):
    """
    Formulario principal para la creación y edición del modelo Producto.
    Aplica clases CSS de Bootstrap y configuraciones de presentación visual.
    """
    class Meta:
        model = Producto
        fields = ['categoria', 'nombre', 'descripcion', 'precio', 'stock', 'imagen_url']
        widgets = {
            'categoria': forms.Select(attrs={
                'class': 'form-control form-select',
            }),
            'nombre': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Nombre del producto...'
            }),
            'descripcion': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 4,
                'placeholder': 'Descripción detallada del producto...'
            }),
            'precio': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': '0.00',
                'step': '0.01',
                'min': '0'
            }),
            'stock': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': '0',
                'min': '0'
            }),
            'imagen_url': forms.URLInput(attrs={
                'class': 'form-control',
                'placeholder': 'https://ejemplo.com/imagen.jpg'
            }),
        }


class CambiarEstadoForm(forms.ModelForm):
    """
    Formulario especializado para la acción de deshabilitar o habilitar
    un registro sin eliminarlo de la base de datos (eliminación lógica).
    """
    class Meta:
        model = Producto
        fields = ['habilitado']


# Alias compatibles con las nomenclaturas de la guía
MiModeloForm = ProductoForm
RegistroForm = ProductoForm
