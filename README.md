# Tienda Online - Backend Django (Evaluación 1)

Sistema backend desarrollado con **Python** y **Django** para la gestión de catálogo, pedidos, usuarios y métricas de una plataforma de comercio electrónico.

---

## 1. Propósito del Proyecto
Este proyecto constituye la base técnica y estructural de una aplicación backend profesional. Implementa:
- Arquitectura modular desacoplada: Proyecto central (`drf`) y Aplicación modular (`tienda_online`).
- Sistema de rutas independientes mediante delegación con `include()`.
- Vistas controladas con inyección de contexto dinámico (variables, listas, diccionarios) y estructuras de control (`for`, `if`).
- Página personalizada para el control y captura de errores HTTP 404.
- Aislamiento de dependencias mediante ambiente virtual (`.venv`).

---

## 2. Estructura del Proyecto

```text
IEI_N4_C3-main2/
├── .gitignore                      # Archivos y carpetas excluidos de Git (.venv, db.sqlite3, etc.)
├── manage.py                       # Utilidad de línea de comandos de Django
├── README.md                       # Documentación del proyecto y guía de instalación
├── requirements.txt                # Dependencias del proyecto
├── drf/                            # Núcleo del proyecto Django
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py                 # Configuración global del proyecto
│   ├── urls.py                     # Enrutador principal (delega a la app)
│   └── wsgi.py
└── tienda_online/                  # Aplicación del proyecto
    ├── __init__.py
    ├── admin.py
    ├── apps.py
    ├── models.py
    ├── tests.py
    ├── urls.py                     # Rutas propias de la aplicación
    ├── views.py                    # Vistas (bienvenida y control 404)
    └── templates/
        ├── 404.html                # Plantilla personalizada de error 404
        └── tienda_online/
            └── bienvenida.html     # Plantilla de bienvenida con diseño y Tailwind CSS
```

---

## 3. Requisitos Previos
- Python 3.10 o superior (recomendado Python 3.11).
- Git instalado.

---

## 4. Guía de Instalación y Ejecución Paso a Paso

### Paso 1: Clonar el repositorio
```bash
git clone https://github.com/47sophiv/Proyecto-backend-IEI-N4-C3.git
cd Proyecto-backend-IEI-N4-C3
```

### Paso 2: Crear el ambiente virtual
Crear el entorno virtual aislado con el nombre `.venv`:
```bash
python -m venv .venv
```

### Paso 3: Activar el ambiente virtual
- **En Windows (PowerShell):**
  ```powershell
  .\.venv\Scripts\Activate.ps1
  ```
  *(Si PowerShell restringe la ejecución de scripts, ejecutar previamente: `Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass`)*

- **En Windows (Símbolo del sistema / CMD):**
  ```cmd
  .\.venv\Scripts\activate.bat
  ```

- **En macOS / Linux:**
  ```bash
  source .venv/bin/activate
  ```

*(Al activarse correctamente, verás `(.venv)` al inicio de la línea de comandos en tu terminal).*

### Paso 4: Instalar las dependencias
Con el ambiente virtual activado, instalar los paquetes registrados:
```bash
pip install -r requirements.txt
```

### Paso 5: Iniciar el servidor de desarrollo
```bash
python manage.py runserver
```

---

## 5. Rutas y Verificación del Proyecto

Una vez que el servidor esté en ejecución en `http://127.0.0.1:8000/`:

1. **Página de Bienvenida (Ruta principal):**
   - URL: `http://127.0.0.1:8000/`
   - Muestra la interfaz moderna de la Tienda Online, los módulos del sistema y el estado del servidor inyectados dinámicamente desde `views.py`.

2. **Página de Error 404 Personalizada:**
   - **Ruta de verificación directa:** `http://127.0.0.1:8000/404/`
   - **En modo producción / demostración:** Si en `drf/settings.py` se establece `DEBUG = False`, al ingresar a cualquier ruta inexistente (por ejemplo `http://127.0.0.1:8000/ruta-no-existe/`), Django activará de forma automática el manejador `handler404` y mostrará la plantilla `404.html`.

---

## 6. Dependencias Utilizadas (`requirements.txt`)

| Paquete | Propósito Técnico |
| :--- | :--- |
| **Django** | Framework principal backend que gestiona el ciclo de peticiones HTTP, rutas, vistas y plantillas. |
| **asgiref** | Especificación estándar para compatibilidad asíncrona (ASGI) y manejo sincrónico/asincrónico. |
| **sqlparse** | Motor de análisis y formateo de lenguaje SQL utilizado internamente por el ORM de Django. |
| **tzdata** | Base de datos de zonas horarias para la gestión correcta de fechas y horas internacionales. |
