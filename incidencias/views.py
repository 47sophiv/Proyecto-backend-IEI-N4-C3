from django.shortcuts import render

# Create your views here.
def bienvenida(request):
    return render(request, 'incidencias/bienvenida.html')

def error_404(request, exception=None):
    return render(request, '404.html', status=404)
   
