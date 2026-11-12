from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test
from .models import Categoria, Herramienta
from django.shortcuts import get_object_or_404, redirect
from django.contrib import messages
from .forms import CategoriaForm, HerramientaForm
from django.db.models.deletion import ProtectedError
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