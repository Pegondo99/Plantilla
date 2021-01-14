from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
import cloudinary.uploader
from Parcial3_Client.services.mensajes_services import get_mensaje_filtered, create_mensaje, get_mensaje
from Parcial3_Client.services.services import authenticate_user

INICIAR_SESION_TEMPLATE = "iniciar-sesion.html"
PRINCIPAL_TEMPLATE = "principal.html"
CREAR_MENSAJE_TEMPLATE = "crear-mensaje.html"
RESPONDER_MENSAJE_TEMPLATE = "responder-mensaje.html"
# Create your views here.


def iniciar_sesion(request):
    return render(request, INICIAR_SESION_TEMPLATE)

@csrf_exempt
def cerrar_sesion(request):
    request.session['usuario'] = None
    return render(request, INICIAR_SESION_TEMPLATE)


def comprobar_response(request, response):
    if isinstance(response, HttpResponse):
        if response.status_code == 401:
            return render(request, INICIAR_SESION_TEMPLATE)

def autenticar_usuario(request):
    id_token = request.POST.get('token')
    idinfo = authenticate_user(id_token)
    comprobar_response(request, idinfo)
    if idinfo is not None:
        request.session['usuario'] = idinfo
        return redirect("/principal")
    else:
        request.session['usuario'] = None
        return render(request, INICIAR_SESION_TEMPLATE)

def cargar_principal(request):
    try:
        usuario = request.session.get('usuario')
    except:
        return render(request, INICIAR_SESION_TEMPLATE)
    if usuario is None:
        return render(request, INICIAR_SESION_TEMPLATE)
    params = {'destino': usuario['email']}
    mensajes= get_mensaje_filtered(usuario['sub'], params)
    return render(request, PRINCIPAL_TEMPLATE, {'mensajes': mensajes})

def crear_mensaje(request):
    try:
        usuario = request.session.get('usuario')
    except:
        return render(request, INICIAR_SESION_TEMPLATE)
    if usuario is None:
        return render(request, INICIAR_SESION_TEMPLATE)
    return render(request, CREAR_MENSAJE_TEMPLATE, {'usuario': usuario})

def enviar_mensaje(request):
    try:
        usuario = request.session.get('usuario')
    except:
        return render(request, INICIAR_SESION_TEMPLATE)

    if usuario is None:
        return render(request, INICIAR_SESION_TEMPLATE)

    foto_url = "https://res.cloudinary.com/dw1sym4yt/image/upload/v1609438278/default_nxezv5.png"
    if len(request.FILES) > 0:
        file = request.FILES['foto']
        result = cloudinary.uploader.upload(file, transformation=[
            {'width': 500, 'crop': 'scale', }])
        foto_url = result["url"]

    destinatario = request.POST.get('destinatario')
    contenido = request.POST.get('contenido')

    mensaje = {'origen': usuario['email'], 'destino': destinatario, 'contenido': contenido, 'imagen': foto_url}

    response = create_mensaje(mensaje, usuario['sub'])
    if response:
        messages.success(request, "¡Has enviado el mensaje!")
    else:
        messages.error(request, "Ha ocurrido un error, tu mensaje no se ha enviado.")

    return redirect("/principal")

def responder_mensaje(request, id):
    try:
        usuario = request.session.get('usuario')
    except:
        return render(request, INICIAR_SESION_TEMPLATE)
    if usuario is None:
        return render(request, INICIAR_SESION_TEMPLATE)

    mensaje= get_mensaje(id, usuario['sub'])

    return render(request, RESPONDER_MENSAJE_TEMPLATE, {'usuario': usuario, 'mensaje':mensaje})

def responder(request):
    try:
        usuario = request.session.get('usuario')
    except:
        return render(request, INICIAR_SESION_TEMPLATE)
    if usuario is None:
        return render(request, INICIAR_SESION_TEMPLATE)
    foto_url = "https://res.cloudinary.com/dw1sym4yt/image/upload/v1609438278/default_nxezv5.png"
    if len(request.FILES) > 0:
        file = request.FILES['foto']
        result = cloudinary.uploader.upload(file, transformation=[
            {'width': 500, 'crop': 'scale', }])
        foto_url = result["url"]
    destinatario = request.POST.get('destinatario')
    contenido = request.POST.get('contenido')

    mensaje = {'origen': usuario['email'], 'destino': destinatario, 'contenido': contenido, 'imagen': foto_url}

    response = create_mensaje(mensaje, usuario['sub'])
    if response:
        messages.success(request, "¡Has respondido al mensaje!")
    else:
        messages.error(request, "Ha ocurrido un error, tu respuesta no se ha enviado.")

    return redirect("/principal")