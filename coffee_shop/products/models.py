from django.db import models

# Create your models here.

class Prodcut(models.Model):
    name = models.TextField(max_length=200, verbose_name="nombre")
    description = models.TextField(max_length=300, verbose_name="descipcion")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="precio")
    available = models.BooleanField(default=True)
    photo = models.ImageField(upload_to="logos", null=True, blank=True, verbose_name="foto")

    def __str__(self):
        return self.name