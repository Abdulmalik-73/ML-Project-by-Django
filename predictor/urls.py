from django.urls import path
from . import views

app_name = 'predictor'

urlpatterns = [
    path('', views.PredictionView.as_view(), name='predict'),
    path('api/predict/', views.api_predict, name='api_predict'),
    path('stats/', views.ModelStatsView.as_view(), name='stats'),
]
