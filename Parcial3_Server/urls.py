from django.urls import path

from Parcial3_Server import views

urlpatterns = [
    path('imagenes/', views.ImagenList.as_view()),
    path('imagenes/<str:id>/', views.ImagenDetail.as_view()),
    path('auth/', views.autenticar_usuario),
]
