from django.db import models

# Create your models here.
class Filmes(models.Model):
    id = models.BigIntegerField(primary_key=True)
    nome = models.CharField(max_length=55)
    categoriaid =  models.BigIntegerField()

class Categoria(models.Model):
    nome = models.CharField(max_length=55)
    idUser = models.BigIntegerField()
   
class Assinaturas(models.Model):
    id = models.BigIntegerField(primary_key=True)
    nome = models.CharField(max_length=55)
    valor = models.DecimalField(max_digits=9,decimal_places=2)

class Usuario(models.Model):
    nome = models.CharField(max_length=55)
    valor = models.DecimalField(max_digits=9,decimal_places=2)
    AssinaturaFK = models.BigIntegerField()

class Favoritos(models.Model):
    Filmeid = models.BigIntegerField()
    Usuarioid = models.BigIntegerField()




