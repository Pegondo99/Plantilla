from mongoengine import *


# Create your models here.

class Imagen(Document):
    foto = StringField()
    descripcion = StringField()
    likes = IntField()
    propietario = StringField()

