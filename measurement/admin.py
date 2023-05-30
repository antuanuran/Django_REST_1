from django.contrib import admin

from .models import Sensor, Measurement


@admin.register(Sensor)
class SensorAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'id']


@admin.register(Measurement)
class SensorAdmin(admin.ModelAdmin):
    list_display = ['sensor', 'temperature', 'id', 'created_at']




