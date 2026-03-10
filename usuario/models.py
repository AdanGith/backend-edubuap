from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class Usuario(AbstractUser):
   
    class Roles(models.IntegerChoices):
        ALUMNO = 0, 'Alumno'
        PROFESOR = 1, 'Profesor'
        ADMINISTRADOR = 2, 'Administrador'

    
    rol = models.IntegerField(choices=Roles.choices, default=Roles.ALUMNO)
    
    correo_institucional = models.EmailField(unique=True, verbose_name='Correo Institucional')
    matricula = models.CharField(max_length=20, unique=True, null=True, blank=True)
    id_docente = models.CharField(max_length=20, unique=True, null=True, blank=True)
    
    apellido_paterno = models.CharField(max_length=50)
    apellido_materno = models.CharField(max_length=50, null=True, blank=True)
    
    USERNAME_FIELD = 'correo_institucional'
    
    REQUIRED_FIELDS = ['username', 'first_name', 'apellido_paterno']

    def __str__(self):
        return f"{self.first_name} {self.apellido_paterno} ({self.get_rol_display()})"


class Perfil(models.Model):
    
    usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE, related_name='perfil')
    
    fotografia_url = models.ImageField(upload_to='perfiles/', null=True, blank=True)
    
    ultima_conexion_at = models.DateTimeField(null=True, blank=True)
    tiempo_conexion_total_seg = models.IntegerField(default=0)
    
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Perfil de {self.usuario.correo_institucional}"
    
    


