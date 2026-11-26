from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Producto, Categoria, Cliente, Pedido, DetallePedido


# ==============================================================================
# Formulario de Autenticación y Registro de Usuarios
# ==============================================================================

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
                'class': 'form-control',
                'placeholder': 'Ingresa tu nombre de usuario...'
            })
        if 'password1' in self.fields:
            self.fields['password1'].label = "Contraseña"
            self.fields['password1'].help_text = "La contraseña debe tener al menos 8 caracteres y no ser común."
            self.fields['password1'].widget.attrs.update({
                'class': 'form-control',
                'placeholder': '••••••••'
            })
        if 'password2' in self.fields:
            self.fields['password2'].label = "Confirmar contraseña"
            self.fields['password2'].help_text = "Ingresa nuevamente la misma contraseña para verificarla."
            self.fields['password2'].widget.attrs.update({
                'class': 'form-control',
                'placeholder': '••••••••'
            })


# ==============================================================================
# Formularios ModelForm para Entidades Principales (Evaluación 3 - Criterio 3)
# ==============================================================================

class ProductoForm(forms.ModelForm):
    """
    Formulario principal para creación y edición de Producto.
    Utiliza ModelForm, define campos explícitamente y personaliza widgets.
    """
    class Meta:
        model = Producto
        fields = ['categoria', 'nombre', 'descripcion', 'precio', 'stock', 'disponible', 'habilitado', 'imagen_url']
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
            'disponible': forms.CheckboxInput(attrs={
                'class': 'form-check-input',
            }),
            'habilitado': forms.CheckboxInput(attrs={
                'class': 'form-check-input',
            }),
            'imagen_url': forms.URLInput(attrs={
                'class': 'form-control',
                'placeholder': 'https://ejemplo.com/imagen.jpg'
            }),
        }


class CategoriaForm(forms.ModelForm):
    """
    Formulario principal para creación y edición de Categoría.
    """
    class Meta:
        model = Categoria
        fields = ['nombre', 'descripcion', 'activo']
        widgets = {
            'nombre': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Nombre de la categoría (ej: Periféricos)...'
            }),
            'descripcion': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 4,
                'placeholder': 'Descripción de la categoría...'
            }),
            'activo': forms.CheckboxInput(attrs={
                'class': 'form-check-input',
            }),
        }


class ClienteForm(forms.ModelForm):
    """
    Formulario principal para creación y edición de Cliente.
    """
    class Meta:
        model = Cliente
        fields = ['nombre', 'email', 'telefono', 'direccion', 'activo']
        widgets = {
            'nombre': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Nombre completo del cliente...'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'cliente@ejemplo.com'
            }),
            'telefono': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': '+56 9 1234 5678'
            }),
            'direccion': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Calle, número, comuna o ciudad...'
            }),
            'activo': forms.CheckboxInput(attrs={
                'class': 'form-check-input',
            }),
        }


class PedidoForm(forms.ModelForm):
    """
    Formulario principal para creación y edición de Pedido.
    """
    class Meta:
        model = Pedido
        fields = ['cliente', 'estado', 'total']
        widgets = {
            'cliente': forms.Select(attrs={
                'class': 'form-control form-select',
            }),
            'estado': forms.Select(attrs={
                'class': 'form-control form-select',
            }),
            'total': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': '0.00',
                'step': '0.01',
                'min': '0'
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


# Alias compatibles con las nomenclaturas de la guía previa
MiModeloForm = ProductoForm
RegistroForm = ProductoForm
