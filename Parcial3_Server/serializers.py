from rest_framework_mongoengine import serializers

from Parcial3_Server.models import Mensaje


class MensajeSerializer(serializers.DocumentSerializer):
    class Meta:
        model = Mensaje
        fields = '__all__'