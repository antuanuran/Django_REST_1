from rest_framework.generics import ListCreateAPIView, CreateAPIView, RetrieveUpdateAPIView

from .models import Sensor, Measurement
from .serializers import SensorSerializer, MeasurementSerializer, SensorDetailSerializer


# Создание (POST) Датчика (сенсора) / Просмотр всех датчиков (GET) - ListCreateAPIView
class SensorView(ListCreateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer


# Обновление (POST) Датчика (сенсора) / Просмотр конкретного датчика (GET) - RetrieveUpdateAPIView
class SensorDetailView(RetrieveUpdateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer


# Создание (POST) меры для датчика. Указываем ссылку на конкретный сенсор и температуру. Время добавится само автоматически
class MeasurementView(CreateAPIView):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer
