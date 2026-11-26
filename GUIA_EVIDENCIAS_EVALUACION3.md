# Guía de Preparación de Evidencias - Evaluación N° 3 (CRUD CBV)

Este documento detalla las capturas de pantalla exactas que debes tomar para construir tu documento PDF de evidencias según lo requerido en la **Evaluación N° 3** y su **Rúbrica de Evaluación**.

---

## 1. Estructura del Documento PDF de Entrega

El PDF debe contener las siguientes secciones:
1. **Portada:**
   - Nombre de la Asignatura: *Programación Backend*
   - Evaluación N° 3: *CRUD mediante Vistas Basadas en Clases (CBV)*
   - Nombre del Estudiante.
   - Enlace al repositorio GitHub: `https://github.com/47sophiv/Proyecto-backend-IEI-N4-C3.git`
2. **Evidencias de Ejecución del Servidor y Pruebas:**
   - Captura de la terminal con el comando `python manage.py test` (31 pruebas OK).
   - Captura de la terminal ejecutando `python manage.py runserver`.
3. **Evidencias del Menú y Navegación:**
   - Captura de la página de inicio (`http://127.0.0.1:8000/`) mostrando la barra de navegación con los enlaces a **Productos**, **Categorías**, **Clientes** y **Pedidos**.
4. **Evidencias del CRUD de Productos (`Producto`):**
   - **ListView:** Listado en `http://127.0.0.1:8000/productos/`.
   - **CreateView:** Formulario en `http://127.0.0.1:8000/productos/crear/` mostrando los widgets personalizados.
   - **DetailView:** Ficha individual en `http://127.0.0.1:8000/productos/<id>/`.
   - **UpdateView:** Formulario de edición en `http://127.0.0.1:8000/productos/<id>/editar/`.
   - **DeleteView:** Pantalla de confirmación en `http://127.0.0.1:8000/productos/<id>/eliminar/` con el botón *"Sí, Confirmar Eliminación"*.
5. **Evidencias del CRUD de Categorías (`Categoria`):**
   - **ListView:** Listado en `http://127.0.0.1:8000/categorias/`.
   - **CreateView:** Formulario en `http://127.0.0.1:8000/categorias/crear/`.
   - **DetailView:** Detalle en `http://127.0.0.1:8000/categorias/<id>/`.
   - **DeleteView:** Pantalla de confirmación previa de borrado.
6. **Evidencias del CRUD de Clientes (`Cliente`):**
   - **ListView:** Listado en `http://127.0.0.1:8000/clientes/`.
   - **CreateView:** Formulario en `http://127.0.0.1:8000/clientes/crear/`.
   - **DetailView:** Ficha en `http://127.0.0.1:8000/clientes/<id>/`.
7. **Evidencias del CRUD de Pedidos (`Pedido`):**
   - **ListView:** Listado en `http://127.0.0.1:8000/pedidos/`.
   - **DetailView:** Visualización en `http://127.0.0.1:8000/pedidos/<id>/` demostrando la integración de las líneas de detalle (`DetallePedido`).
8. **Evidencias de Control de Versiones (Git):**
   - Captura del historial de commits en GitHub o mediante comando `git log --oneline -n 8`.
