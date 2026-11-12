from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('herramientas/', views.herramienta_lista, name='herramienta_lista'),
    path('herramientas/crear/', views.herramienta_crear, name='herramienta_crear'),
    path('herramientas/<int:id>/editar/', views.herramienta_editar, name='herramienta_editar'),
    path('herramientas/<int:id>/eliminar/', views.herramienta_eliminar, name='herramienta_eliminar'),
    path('categorias/', views.categoria_lista, name='categoria_lista'),
    path('categorias/crear/', views.categoria_crear, name='categoria_crear'),
    path('categorias/<int:id>/editar/', views.categoria_editar, name='categoria_editar'),
    path('categorias/<int:id>/eliminar/', views.categoria_eliminar, name='categoria_eliminar'),
    path('herramientas/<int:id>/', views.herramienta_detalle, name='herramienta_detalle'),
    path('catalogo/', views.catalogo, name='catalogo'),
    path('solicitud/agregar/<int:id>/', views.agregar_solicitud, name='agregar_solicitud'),
    path('solicitud/', views.ver_solicitud, name='ver_solicitud'),
    path('solicitud/quitar/<int:id>/', views.quitar_solicitud, name='quitar_solicitud'),
    path('solicitud/confirmar/', views.confirmar_solicitud, name='confirmar_solicitud'),
    path('mis-prestamos/', views.mis_prestamos, name='mis_prestamos'),
    path('prestamos/<int:id>/cancelar/', views.cancelar_prestamo, name='cancelar_prestamo'),
    path('prestamos/todos/', views.todos_prestamos, name='todos_prestamos'),
    path('prestamos/<int:id>/activar/', views.activar_prestamo, name='activar_prestamo'),
    path('prestamos/<int:id>/devolver/', views.devolver_prestamo, name='devolver_prestamo'),
]