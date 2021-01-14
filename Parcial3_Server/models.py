from datetime import datetime
from mongoengine import Document, StringField, DateTimeField


# Create your models here.

class Mensaje(Document):
    origen = StringField(null=False)
    destino = StringField(null=False)
    contenido = StringField(null=False)
    fecha = DateTimeField(default=datetime.utcnow)
    imagen = StringField()