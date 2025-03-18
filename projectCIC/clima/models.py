from django.db import models

# Create your models here.

class Datos(models.Model):
    ciudad = models.CharField(max_length=20)
    temperatura = models.FloatField()
    humedad = models.FloatField()
    
    def __str__(self):
        return f"{self.ciudad} - Temp: {self.temperatura}, Hum: {self.humedad}"

    class Meta:
        db_table = 'datos'