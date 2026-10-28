from django.db import models
from productos.models import Producto

class Pedido(models.Model):
    cliente = models.CharField(max_length=150, verbose_name="Nombre del cliente")
    telefono = models.CharField(max_length=20, verbose_name="Teléfono de contacto")
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE, verbose_name="Prenda / Tela solicitada")
    
    # Medidas básicas de sastrería
    pecho = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True, verbose_name="Pecho (cm)")
    cintura = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True, verbose_name="Cintura (cm)")
    largo = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True, verbose_name="Largo (cm)")
    
    fecha_pedido = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de solicitud")
    completado = models.BooleanField(default=False, verbose_name="¿Pedido entregado?")

    def __str__(self):
        return f"Pedido de {self.cliente} - {self.producto.nombre}"
