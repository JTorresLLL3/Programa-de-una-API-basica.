"""
Este archivo contiene todas las vistas relacionadas con el modelo Usuario, incluyendo el registro, búsqueda, modificación y eliminación de usuarios. 
Además, tiene una vista index simple para pruebas iniciales.

"""

from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.shortcuts import render, redirect
from polls.models import Usuario

# Create your views here.
def index(request):
    return HttpResponse("Hola mundo, este es el index de polls.")

# Registro de usuario
def registro(request):
    if request.method == "POST":
        nombre = request.POST.get('nombre')
        edad = request.POST.get('edad')
        correo = request.POST.get('correo')

        nuevo_usuario = Usuario(nombre=nombre, edad=edad, correo=correo)
        nuevo_usuario.save()
        
        return redirect('busqueda')  # Redirige a la búsqueda.

    return render(request, 'registro.html')

# Búsqueda de usuarios
def busqueda(request):
    query = request.GET.get("nombre", "")  # Obtiene el nombre de la búsqueda.
    if query:
        usuarios = Usuario.objects.filter(nombre__icontains=query)  # Busca coincidencias parciales.
        mensaje = "No se encontraron usuarios." if not usuarios else ""
    else:
        usuarios = Usuario.objects.all()  # Muestra todos los usuarios si no hay búsqueda.
        mensaje = ""

    return render(request, "busqueda.html", {"usuarios": usuarios, "mensaje": mensaje})

# Modificación de usuarios.
def modificar_usuario(request, usuario_id):
    usuario = get_object_or_404(Usuario, id=usuario_id)

    if request.method == "POST":
        usuario.nombre = request.POST["nombre"]
        usuario.edad = request.POST["edad"]
        usuario.correo = request.POST["correo"]
        usuario.save()
        return redirect("busqueda")  # Redirige a la búsqueda después de modificar

    return render(request, "modificar.html", {"usuario": usuario})

# Eliminación de usuarios.
def eliminar_usuario(request, usuario_id):
    usuario = get_object_or_404(Usuario, id=usuario_id)

    if request.method == "POST":
        usuario.delete()
        return redirect("busqueda")  # Redirige a la búsqueda después de eliminar

    return render(request, "eliminar.html", {"usuario": usuario})