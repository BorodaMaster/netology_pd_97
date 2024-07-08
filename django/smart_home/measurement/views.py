from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView
from rest_framework.response import Response
from .models import Sensor, Measurement
from .serializers import MeasurementSerializer, SensorDetailSerializer


class SensorsView(ListCreateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer

    def post(self, request, *args, **kwargs):

        return self.create(request, *args, **kwargs)


class SensorView(RetrieveUpdateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer

    def get_queryset(self, pk):
        sensor = Sensor.objects.filter(id=pk)
        measurement = Measurement.objects.filter(sensor_id=pk)

        serializer_sensor = SensorDetailSerializer(sensor, many=True).data
        serializer_measurement = MeasurementSerializer(measurement, many=True).data

        data = serializer_sensor[0]
        data["measurements"] = serializer_measurement

        return Response(data)


class Measurements(ListCreateAPIView):
    serializer_class = MeasurementSerializer

    def post(self, request, *args, **kwargs):

        return self.create(request, *args, **kwargs)
