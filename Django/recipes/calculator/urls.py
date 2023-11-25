from django.urls import path
from calculator.views import dish_view

urlpatterns = [
    path('<dish>/', dish_view, name='dish'),
]