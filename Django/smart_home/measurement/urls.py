from django.urls import path
from .views import SensorView, MeasurementCreate, SensorUpdate


urlpatterns = [
    path('sensors/', SensorView.as_view()),
    path('sensors/<pk>/', SensorUpdate.as_view()),
    path('measurements/', MeasurementCreate.as_view()),
]

