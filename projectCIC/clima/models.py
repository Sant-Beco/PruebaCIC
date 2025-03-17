from django.db import models

# Create your models here.

class datos(models.Model):
    id = models.AutoField(primary_key=True)
    ciudad = models.CharField(max_length=20)
    temperatura = models.FloatField(max_length=4)
    humedad = models.FloatField(max_length=4)
    
    def __str__(self):
        return self.datos

    class Meta:
        managed = True
        db_table = 'datos'