
# Herramientas en Común

Aplicación web desarrollada con Django para administrar el inventario y los préstamos de herramientas de la Junta de Vecinos Villa Los Aromos.

## Funcionalidades

- Inicio y cierre de sesión.
- Administración de herramientas y categorías (CRUD).
- Búsqueda y filtrado de herramientas.
- Solicitud de hasta 3 herramientas mediante sesiones.
- Registro y cancelación de préstamos.
- Activación de préstamos y registro de devoluciones.
- Control de acceso para socios y encargados.

## Tecnologías

- Python
- Django
- SQLite
- HTML
- Git y GitHub

## Instalación

1. Clonar el repositorio.
2. Crear y activar un entorno virtual.
3. Instalar dependencias:

    pip install -r requirements.txt

4. Crear un archivo .env a partir de .env.example y configurar SECRET_KEY y DEBUG.
5. Crear las tablas:

    python manage.py migrate

6. Cargar los datos de prueba:

    python manage.py loaddata herramientas.json

7. Crear los usuarios de prueba y asignar is_staff=True al encargado.

8. Ejecutar el servidor:

    python manage.py runserver

9. Abrir http://127.0.0.1:8000/

## Usuarios de prueba

- admin: superusuario.
- encargado: usuario con is_staff=True.
- socio: usuario normal.

Las contraseñas deben configurarse localmente y no se incluyen en el repositorio.

## Uso de inteligencia artificial

Consultar BITACORA_IA.md para conocer los usos documentados de IA durante el desarrollo.
