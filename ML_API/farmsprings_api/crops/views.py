from django.shortcuts import render
from rest_framework.views import APIView
from .models import *



import os
import pickle
import pandas as pd
import numpy as np
from django.conf import settings
from .apps import CropsConfig
from rest_framework import views
from rest_framework import status
from rest_framework.response import Response
from sklearn.linear_model import LinearRegression


class Predict(views.APIView):
    def post(self, request):
        crops_dataset = Pear.objects.all()
        print(type(crops_dataset))
        # django.db.models.query.QuerySet.

        # print(CropsConfig.crops_dataset)
        predictions = []
        # for entry in request.data:
        path = os.path.join(settings.MODEL_ROOT, "test")
        with open(path, 'rb') as file:
            model = pickle.load(file)

        example_test_set = np.array([155,16.24267857142857,11.82642857142857,21.888035714285717,3.874553571428571,8.926404761904763,624.8483333333334,7.135535714285715,4.268392857142857,1.6282142857142858,1406.7625000000005,11.716607142857145,48.830357142857146,75.75785714285715,15.811785714285715,1011.03375,11.715,4.907857142857144,1.949464285714286,11.835982142857144,0.0128571428571428,0.0128571428571428,17.539464285714285,10.287857142857144,18.07857142857143,18.317857142857147,18.584821428571427,18.821428571428573,19.64017857142857,20.38482142857143,0,0,0,10.061607142857143,4,19,1,1,0])
        example_test_set = example_test_set.reshape(1, -1)
        result = model.predict(example_test_set)
        predictions.append(result[0])
        print(predictions)

        return Response({"prediction": predictions}, status=status.HTTP_200_OK, content_type='application/json')
