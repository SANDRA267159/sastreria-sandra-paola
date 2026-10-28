from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    ROLES = (
        ('admin', 'Administrador'),
        ('manager', 'Gestor de Ventas'),
        ('customer', 'Usuario / Cliente'),
    )
    
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=20, choices=ROLES, default='customer')
    
    # Medidas corporales para las prendas a medida
    pecho_cm = models.FloatField(null=True, blank=True, verbose_name="Pecho/Busto (cm)")
    cintura_cm = models.FloatField(null=True, blank=True, verbose_name="Cintura (cm)")
    cadera_cm = models.FloatField(null=True, blank=True, verbose_name="Cadera (cm)")
    largo_brazo_cm = models.FloatField(null=True, blank=True, verbose_name="Largo de Brazo (cm)")

    def __str__(self):
        return f"{self.user.username} - {self.get_role_display()}"
