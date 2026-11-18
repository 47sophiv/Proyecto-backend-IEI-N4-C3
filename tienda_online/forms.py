from django import forms
from .models import Producto, Categoria


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
