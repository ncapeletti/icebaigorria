from django.db import models
from django.utils import timezone


class Persons(models.Model):
    idpersona = models.SmallIntegerField()
    nombre = models.CharField(max_length=200)
    apellido = models.CharField(max_length=200)
    observaciones = models.TextField()
    fechanac=models.DateTimeField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.nombre