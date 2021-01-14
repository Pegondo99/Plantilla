import django_mongoengine_filter

from Parcial3_Server.models import Mensaje


class MensajeFilter(django_mongoengine_filter.FilterSet):
    contenido = django_mongoengine_filter.filters.StringFilter(lookup_type='icontains')

    class Meta:
        model = Mensaje
        fields = ['destino', 'origen', 'fecha']