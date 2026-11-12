from django.db import models

# Create your models here.
class Categoria(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    descripcion = models.TextField()

    def __str__(self):
        return self.nombre

class Herramienta(models.Model):
    ESTADOS = [
        ('Bueno', 'Bueno'),
        ('Regular', 'Regular'),
        ('En reparación', 'En reparación'),
    ]

    codigo = models.CharField(max_length=20, unique=True)
    nombre = models.CharField(max_length=100)
    categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT)
    estado = models.CharField(max_length=20, choices=ESTADOS)
    disponible = models.BooleanField(default=True)
    fecha_ingreso = models.DateField()

    def __str__(self):
        return self.nombre

class Prestamo(models.Model):
    ESTADOS = [
        ('Pendiente', 'Pendiente'),
        ('Activo', 'Activo'),
        ('Devuelto', 'Devuelto'),
        ('Cancelado', 'Cancelado'),
    ]

    socio = models.ForeignKey('auth.User', on_delete=models.PROTECT)
    herramienta = models.ForeignKey(Herramienta, on_delete=models.PROTECT)
    fecha_solicitud = models.DateTimeField(auto_now_add=True)
    fecha_devolucion_esperada = models.DateField()
    fecha_devolucion_real = models.DateField(null=True, blank=True)
    estado = models.CharField(max_length=20, choices=ESTADOS, default='Pendiente')

    def __str__(self):
        return f"{self.socio.username} - {self.herramienta.nombre}"