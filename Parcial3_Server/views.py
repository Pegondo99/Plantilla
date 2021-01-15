import json

from google.auth.transport import requests
from django.core.cache import cache
from django.http import HttpResponse, Http404
from google.oauth2 import id_token
from rest_framework_mongoengine import generics

from Parcial3.settings import GOOGLE_CLIENT_ID
from Parcial3_Server.filters import ImagenFilter
from Parcial3_Server.models import Imagen
from Parcial3_Server.serializers import ImagenSerializer


def autenticar_usuario(request):
    token = request.GET.get('token')
    try:
        # Specify the CLIENT_ID of the app that accesses the backend:
        idinfo = id_token.verify_oauth2_token(token, requests.Request(), GOOGLE_CLIENT_ID)

        # Or, if multiple clients access the backend server:
        # idinfo = id_token.verify_oauth2_token(token, requests.Request())
        # if idinfo['aud'] not in [CLIENT_ID_1, CLIENT_ID_2, CLIENT_ID_3]:
        #     raise ValueError('Could not verify audience.')

        # If auth request is from a G Suite domain:
        # if idinfo['hd'] != GSUITE_DOMAIN_NAME:
        #     raise ValueError('Wrong hosted domain.')

        # ID token is valid. Get the user's Google Account ID from the decoded token.
        # userid = idinfo['sub']
        cache.set(idinfo['sub'], idinfo['sub'], idinfo['exp'])

    except ValueError:
        # Invalid token
        raise Http404("Invalid token")
    return HttpResponse(json.dumps(idinfo), content_type='application/json')


##############################
# Vistas API Externa Datos abiertos Malaga
##############################
""""
def ayuntamiento_actividades(requests):
    json_actividades = json.dumps(
        get_actividades_ayuntamiento())
    return HttpResponse(json_actividades, content_type='application/json')


def calidad_aire(requests):
    agno = requests.GET.get('agno', datetime.now())
    json_calidad_aire = json.dumps(get_calidad_aire({'agno': agno}))
    return HttpResponse(json_calidad_aire, content_type='application/json')


def monumentos_malaga(requests):
    limit = requests.GET.get('limit', '5')
    json_monumentos = geojson.dumps(get_monumentos({'limit': limit}))
    return HttpResponse(json_monumentos, content_type='application/vnd.geo+json')
"""

##############################
# Vistas coleccion Imágenes
##############################

class ImagenList(generics.ListCreateAPIView):
    queryset = Imagen.objects.order_by('-likes')
    serializer_class = ImagenSerializer

    def get(self, request, *args, **kwargs):
        token = request.headers['Authorization']
        print("TOKEN SERVER "+token)
        result = cache.get(token)
        if result is None:
            return HttpResponse('Unauthorized', status=401)
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        token = request.headers['Authorization']
        result = cache.get(token)
        if result is None:
            return HttpResponse('Unauthorized', status=401)
        return self.create(request, *args, **kwargs)

    def filter_queryset(self, queryset):
        descripcion = self.request.query_params.get("descripcion", None)
        if descripcion:
            queryset = queryset.filter(descripcion__contains=descripcion)  # Filtra sobre arrays sin poner __in

        return queryset




class ImagenDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Imagen.objects.all()
    serializer_class = ImagenSerializer

    def get(self, request, *args, **kwargs):
        token = request.headers['Authorization']
        result = cache.get(token)
        if result is None:
            return HttpResponse('Unauthorized', status=401)
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        token = request.headers['Authorization']
        result = cache.get(token)
        if result is None:
            return HttpResponse('Unauthorized', status=401)
        return self.update(request, *args, **kwargs)

    #def delete(self, request, *args, **kwargs):
    #    token = request.headers['Authorization']
    #    result = cache.get(token)
    #    if result is None:
    #        return HttpResponse('Unauthorized', status=401)
    #    return self.destroy(request, *args, **kwargs)
