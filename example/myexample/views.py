from django.shortcuts import render, redirect
from polls.models import Usuario
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, redirect

# Vista para registrar nuevos usuarios
def registro(request):
    if request.method == "POST":
        nombre = request.POST.get('nombre')
        edad = request.POST.get('edad')
        correo = request.POST.get('correo')

        # Crear y guardar el nuevo usuario
        nuevo_usuario = Usuario(nombre=nombre, edad=edad, correo=correo)
        nuevo_usuario.save()
        
        return redirect('busqueda')  # Redirigir a la página de búsqueda

    return render(request, 'registro.html')


def busqueda(request):
    if "nombre" in request.GET:
        nombre = request.GET["nombre"]
        usuarios = Usuario.objects.filter(nombre__icontains=nombre)

        if usuarios:
            return render(request, "busqueda.html", {"usuarios": usuarios})
        else:
            return render(request, "busqueda.html", {"mensaje": "No se encontraron usuarios con ese nombre."})

    return render(request, "busqueda.html")

from django.shortcuts import render, get_object_or_404, redirect
from polls.models import Usuario

def modificar_usuario(request, id):
    usuario = get_object_or_404(Usuario, id=id)

    if request.method == 'POST':
        # Obtener los datos del formulario
        nombre = request.POST.get('nombre')
        edad = request.POST.get('edad')
        correo = request.POST.get('correo')

        # Actualizar los datos del usuario
        usuario.nombre = nombre
        usuario.edad = edad
        usuario.correo = correo
        usuario.save()

        return redirect('busqueda')  # Redirigir a la página de búsqueda

    # Si no es POST, mostrar el formulario con los datos actuales del usuario
    return render(request, 'modificar.html', {'usuario': usuario})

def eliminar_usuario(request, id):
    usuario = get_object_or_404(Usuario, id=id)
    if request.method == 'POST':
        usuario.delete()
        return redirect('busqueda')
    return render(request, 'eliminar.html', {'usuario': usuario})
