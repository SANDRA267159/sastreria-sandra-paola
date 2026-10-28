from django.db import models

class Producto(models.Model):
    nombre = models.CharField(max_length=100, verbose_name="Nombre de la prenda / tela")
    descripcion = models.TextField(blank=True, null=True, verbose_name="Descripción")
    precio = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Precio base")
    stock = models.IntegerField(default=0, verbose_name="Disponibilidad / Metros")
    imagen = models.ImageField(upload_to='productos/', blank=True, null=True, verbose_name="Imagen")

    def __str__(self):
        return self.nombre
