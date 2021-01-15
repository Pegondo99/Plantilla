from django.urls import path
from Parcial3_Client import views

urlpatterns = [
    path('', views.iniciar_sesion),
    path('autenticarUsuario/', views.autenticar_usuario, name='autenticar'),
    path('cerrarSesion/', views.cerrar_sesion, name='cerrar_sesion'),

    path('principal/', views.cargar_principal, name='principal'),
    path('crearMensaje/', views.crear_mensaje, name='crear_mensaje'),
    path('enviarMensaje/', views.enviar_mensaje, name='enviar'),
    path('responderMensaje/<str:id>', views.responder_mensaje, name='responder_mensaje'),
    path('responder/', views.responder, name='responder'),

    path('subir-imagen/', views.crear_imagen, name='crear-imagen'),
    path('dar-like/<str:id>', views.dar_like, name='dar-like'),
    path('eliminar-imagen/<str:id>', views.eliminar_imagen, name='eliminar-imagen'),
    path('modificar-desc/<str:id>', views.modificar_desc, name='modificar-desc')
]
