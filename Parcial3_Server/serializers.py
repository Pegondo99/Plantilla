from rest_framework_mongoengine import serializers

from Parcial3_Server.models import Imagen


class ImagenSerializer(serializers.DocumentSerializer):
    class Meta:
        model = Imagen
        fields = '__all__'