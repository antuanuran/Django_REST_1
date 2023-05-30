from django.db import models


class Sensor(models.Model):
    # id
    name = models.CharField(max_length=40)
    description = models.TextField(null=True, blank=True)
    # measurements


class Measurement(models.Model):
    # id
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE, related_name='measurements')
    temperature = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
