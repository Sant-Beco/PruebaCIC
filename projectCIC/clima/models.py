from django.db import models

class Datos(models.Model):
    ciudad = models.CharField(max_length=20)
    temperatura = models.FloatField()
    humedad = models.FloatField()

    class Meta:
        db_table = "datos"
        verbose_name = "Dato"
        verbose_name_plural = "Datos"
        ordering = ["ciudad"]

    def __str__(self):
        return f"{self.ciudad} - Temp: {self.temperatura}°C, Hum: {self.humedad}%"
