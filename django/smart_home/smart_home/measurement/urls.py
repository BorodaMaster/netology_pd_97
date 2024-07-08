from django.urls import path
from django.contrib import admin
from .views import SensorsView, SensorView, Measurements

urlpatterns = [
    path('sensors/', SensorsView.as_view()),
    path('sensors/<pk>/', SensorView.as_view()),
    path('measurements/', Measurements.as_view()),
    path('admin/', admin.site.urls),
]
