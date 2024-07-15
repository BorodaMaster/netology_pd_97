from django.urls import path
from django.contrib import admin
from .views import SensorsView, SensorDetailsView, Measurements

urlpatterns = [
    path('sensors/', SensorsView.as_view()),
    path('sensors/<pk>/', SensorDetailsView.as_view()),
    path('measurements/', Measurements.as_view()),
    path('admin/', admin.site.urls),
]
