from django.urls import path, include
from rest_framework import routers
from . import views
from django.conf.urls import url

urlpatterns = [
    path('', views.index, name='index'),
    path('intro/', views.intro, name='intro'),
    path('climate/', views.climate, name='climate'),
    path('prod_info/', views.prod_info, name='prod_info'),
    path('prod_change/', views.prod_change, name='prod_change'),
    path('prediction_prod/', views.prediction_prod, name='prediction_prod'),
    path('prediction_crops_prod/', views.prediction_crops_prod, name='prediction_crops_prod'),
    path('crops_trend/', views.crops_trend, name='crops_trend'),
    path('predict/', views.Predict.as_view(), name="predict"),
    path('predict_crop/', views.Predict_crop.as_view(), name="predict_crop"),
    path('trend/', views.Trend.as_view(), name="trend"),
    path('change/', views.Change.as_view(), name="change"),
    path('api_result/', views.ResultAPIView.as_view(), name="api_result"),
]

from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns += staticfiles_urlpatterns()

# urlpatterns = [
#     path('predict/', Predict.as_view(), name='predict')
# ]

