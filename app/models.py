from django.db import models

# Create your models here.

class Profesor(models.Model):
    nombre = models.CharField(
        'nombre',
        max_length=50
    )
    email = models.EmailField()
    
    