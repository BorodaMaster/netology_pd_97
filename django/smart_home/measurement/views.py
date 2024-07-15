from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView
from .models import Sensor
from .serializers import MeasurementSerializer, SensorSerializer, SensorDetailSerializer


class SensorsView(ListCreateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer

    def post(self, request, *args, **kwargs):

        return self.create(request, *args, **kwargs)


class SensorDetailsView(RetrieveUpdateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer


class Measurements(ListCreateAPIView):
    serializer_class = MeasurementSerializer

    def post(self, request, *args, **kwargs):

        return self.create(request, *args, **kwargs)
