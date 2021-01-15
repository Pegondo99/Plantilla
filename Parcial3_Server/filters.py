import django_mongoengine_filter

from Parcial3_Server.models import Imagen


class ImagenFilter(django_mongoengine_filter.FilterSet):
    contenido = django_mongoengine_filter.filters.StringFilter(lookup_type='icontains')

    class Meta:
        model = Imagen
        fields = ['descripcion']