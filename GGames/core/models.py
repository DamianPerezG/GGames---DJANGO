from django.db import models
from django.contrib.auth import get_user_model
from django.conf import settings
from django.db.models import Model

class UserProfile(models.Model):
    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE)
    role = models.CharField(max_length=20, choices=settings.ROLES)

    def __str__(self):
        return self.user.username + '-' + self.role

class NewUser(models.Model):
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    usuario= models.CharField(max_length=20)
    contraseña= models.CharField(max_length=20)

class UserLogin(models.Model):
    usuario=models.CharField(max_length=20)
    contraseña=models.CharField

class Juegos(models.Model):

    código = models.IntegerField(4)
    nombre = models.CharField (max_length=30)
    categoría = models.CharField(max_length=15)
    Imagen = models.ImageField(upload_to='img')
    Descripción = models.TextField(max_length=200)
    Stock = models.IntegerField
    Precio = models.DecimalField(decimal_places=3, max_digits=6)


#preguntar: usuarios y login (hechos en base de dato o los que se puedan registrar por la app?)