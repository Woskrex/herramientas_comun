from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test
from .models import Categoria, Herramienta
from django.shortcuts import get_object_or_404, redirect
from django.contrib import messages
from .forms import CategoriaForm, HerramientaForm
from django.db.models.deletion import ProtectedError
from django.views.decorators.http import require_POST
from .models import Prestamo
from django.utils import timezone
from datetime import timedelta
from django.db import transaction
# Create your views here.

@login_required
def inicio(request):
    return render(request, 'inicio.html')

def es_encargado(user):
    return user.is_authenticated and user.is_staff

def inicio(request):
    return render(request, 'inicio.html')

@login_required
@user_passes_test(es_encargado)
def herramienta_lista(request):
    herramientas = Herramienta.objects.all()

    busqueda = request.GET.get('buscar', '')
    categoria = request.GET.get('categoria', '')

    if busqueda:
        herramientas = herramientas.filter(nombre__icontains=busqueda)

    if categoria:
        herramientas = herramientas.filter(categoria_id=categoria)

    categorias = Categoria.objects.all()

    return render(request, 'herramienta_list.html', {
        'herramientas': herramientas,
        'categorias': categorias
    })

@login_required
@user_passes_test(es_encargado)
def herramienta_crear(request):
    if request.method == 'POST':
        form = HerramientaForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, 'Herramienta creada correctamente')
            return redirect('herramienta_lista')
    else:
        form = HerramientaForm()

    return render(request, 'herramienta_form.html', {'form': form})

@login_required
@user_passes_test(es_encargado)
def herramienta_editar(request, id):
    herramienta = get_object_or_404(Herramienta, id=id)

    if request.method == 'POST':
        form = HerramientaForm(request.POST, instance=herramienta)

        if form.is_valid():
            form.save()
            messages.success(request, 'Herramienta actualizada correctamente')
            return redirect('herramienta_lista')
    else:
        form = HerramientaForm(instance=herramienta)

    return render(request, 'herramienta_form.html', {'form': form})

@login_required
@user_passes_test(es_encargado)
def herramienta_eliminar(request, id):
    herramienta = get_object_or_404(Herramienta, id=id)

    if request.method == 'POST':
        herramienta.delete()
        messages.success(request, 'Herramienta eliminada correctamente')
        return redirect('herramienta_lista')

    return render(request, 'herramienta_confirm_delete.html', {
        'herramienta': herramienta
    })

@login_required
@user_passes_test(es_encargado)
def categoria_lista(request):
    categorias = Categoria.objects.all()
    return render(request, 'categoria_list.html', {
        'categorias': categorias
    })

@login_required
@user_passes_test(es_encargado)
def categoria_crear(request):
    if request.method == 'POST':
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Categoría creada correctamente')
            return redirect('categoria_lista')
    else:
        form = CategoriaForm()

    return render(request, 'categoria_form.html', {'form': form})


@login_required
@user_passes_test(es_encargado)
def categoria_editar(request, id):
    categoria = get_object_or_404(Categoria, id=id)

    if request.method == 'POST':
        form = CategoriaForm(request.POST, instance=categoria)
        if form.is_valid():
            form.save()
            messages.success(request, 'Categoría actualizada correctamente')
            return redirect('categoria_lista')
    else:
        form = CategoriaForm(instance=categoria)

    return render(request, 'categoria_form.html', {'form': form})

@login_required
@user_passes_test(es_encargado)
def categoria_crear(request):
    if request.method == 'POST':
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Categoría creada correctamente')
            return redirect('categoria_lista')
    else:
        form = CategoriaForm()

    return render(request, 'categoria_form.html', {'form': form})


@login_required
@user_passes_test(es_encargado)
def categoria_editar(request, id):
    categoria = get_object_or_404(Categoria, id=id)

    if request.method == 'POST':
        form = CategoriaForm(request.POST, instance=categoria)
        if form.is_valid():
            form.save()
            messages.success(request, 'Categoría actualizada correctamente')
            return redirect('categoria_lista')
    else:
        form = CategoriaForm(instance=categoria)

    return render(request, 'categoria_form.html', {'form': form})

@login_required
@user_passes_test(es_encargado)
def categoria_eliminar(request, id):
    categoria = get_object_or_404(Categoria, id=id)

    if request.method == 'POST':
        try:
            categoria.delete()
            messages.success(request, 'Categoría eliminada correctamente')
        except ProtectedError:
            messages.error(request, 'No puedes eliminar una categoría con herramientas asociadas')

        return redirect('categoria_lista')

    return render(request, 'categoria_confirm_delete.html', {
        'categoria': categoria
    })

@login_required
@user_passes_test(es_encargado)
def herramienta_detalle(request, id):
    herramienta = get_object_or_404(Herramienta, id=id)

    return render(request, 'herramienta_detail.html', {
        'herramienta': herramienta
    })

@login_required
def catalogo(request):
    herramientas = Herramienta.objects.filter(
        disponible=True
    ).exclude(estado='En reparación')

    return render(request, 'catalogo.html', {
        'herramientas': herramientas
    })

@login_required
@require_POST
def agregar_solicitud(request, id):
    herramienta = get_object_or_404(Herramienta, id=id)
    solicitud = request.session.get('solicitud', [])

    if not herramienta.disponible or herramienta.estado == 'En reparación':
        messages.error(request, 'La herramienta no está disponible')

    elif id in solicitud:
        messages.error(request, 'La herramienta ya está en tu solicitud')

    elif len(solicitud) >= 3:
        messages.error(request, 'Solo puedes solicitar 3 herramientas')

    else:
        solicitud.append(id)
        request.session['solicitud'] = solicitud
        messages.success(request, 'Herramienta agregada correctamente')

    return redirect('catalogo')

@login_required
def ver_solicitud(request):
    ids = request.session.get('solicitud', [])
    herramientas = Herramienta.objects.filter(id__in=ids)

    return render(request, 'solicitud.html', {
        'herramientas': herramientas
    })

@login_required
@require_POST
def quitar_solicitud(request, id):
    solicitud = request.session.get('solicitud', [])

    if id in solicitud:
        solicitud.remove(id)
        request.session['solicitud'] = solicitud
        request.session.modified = True
        messages.success(request, 'Herramienta quitada de la solicitud')

    return redirect('ver_solicitud')

@login_required
@require_POST
def confirmar_solicitud(request):
    ids = request.session.get('solicitud', [])

    if not ids:
        messages.error(request, 'La solicitud está vacía')
        return redirect('ver_solicitud')

    with transaction.atomic():
        herramientas = list(
            Herramienta.objects.select_for_update().filter(id__in=ids)
        )

        if len(herramientas) != len(ids) or any(
            not h.disponible or h.estado == 'En reparación'
            for h in herramientas
        ):
            messages.error(request, 'Una herramienta ya no está disponible')
            return redirect('ver_solicitud')

        for herramienta in herramientas:
            Prestamo.objects.create(
                socio=request.user,
                herramienta=herramienta,
                fecha_devolucion_esperada=timezone.localdate() + timedelta(days=7),
                estado='Pendiente'
            )

            herramienta.disponible = False
            herramienta.save()

    del request.session['solicitud']
    messages.success(request, 'Solicitud confirmada correctamente')

    return redirect('mis_prestamos')

@login_required
def mis_prestamos(request):
    prestamos = Prestamo.objects.filter(
        socio=request.user
    ).order_by('-fecha_solicitud')

    return render(request, 'mis_prestamos.html', {
        'prestamos': prestamos
    })


@login_required
@require_POST
def cancelar_prestamo(request, id):
    prestamo = get_object_or_404(
        Prestamo,
        id=id,
        socio=request.user,
        estado='Pendiente'
    )

    prestamo.estado = 'Cancelado'
    prestamo.save()

    prestamo.herramienta.disponible = True
    prestamo.herramienta.save()

    messages.success(request, 'Préstamo cancelado correctamente')
    return redirect('mis_prestamos')


@login_required
@user_passes_test(es_encargado)
def todos_prestamos(request):
    prestamos = Prestamo.objects.all().order_by('-fecha_solicitud')

    return render(request, 'todos_prestamos.html', {
        'prestamos': prestamos
    })


@login_required
@user_passes_test(es_encargado)
@require_POST
def activar_prestamo(request, id):
    prestamo = get_object_or_404(Prestamo, id=id, estado='Pendiente')
    prestamo.estado = 'Activo'
    prestamo.save()

    messages.success(request, 'Préstamo activado correctamente')
    return redirect('todos_prestamos')


@login_required
@user_passes_test(es_encargado)
@require_POST
def devolver_prestamo(request, id):
    prestamo = get_object_or_404(Prestamo, id=id, estado='Activo')

    prestamo.estado = 'Devuelto'
    prestamo.fecha_devolucion_real = timezone.localdate()
    prestamo.save()

    prestamo.herramienta.disponible = True
    prestamo.herramienta.save()

    messages.success(request, 'Devolución registrada correctamente')
    return redirect('todos_prestamos')