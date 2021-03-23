from django.urls import path, include
from rest_framework import routers
from .views import Predict
from django.conf.urls import url

urlpatterns = [
    url(r'^predict/', Predict.as_view(), name="predict")
]

# urlpatterns = [
#     path('predict/', Predict.as_view(), name='predict')
# ]