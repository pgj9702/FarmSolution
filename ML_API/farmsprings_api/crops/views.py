from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.views import APIView
from . import models
from django.shortcuts import render
from django.http import HttpResponse

from django.template import loader
from django.shortcuts import render
import json

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

# index.html, 홈페이지
def index(request):
    context = {
        "value": 2
    }
    return render(request, 'index.html', context)

# intro.html, 페이지 소개
def intro(request):
    return render(request, 'intro.html')

# climate.html, 기상정보
def climate(request):
    return render(request, 'climate.html')

# prod_info.html, 농작물 생산 정보
def prod_info(request):
    return render(request, 'prod_info.html')

# prod_change.html, 농작물 생산량 변화
def prod_change(request):
    return render(request, 'prod_change.html')

# prediction_prod.html, 농작물 생산성 예측
def prediction_prod(request):
    return render(request, 'prediction_prod.html')

# prediction_crops_prod.html, 작물별 생산성 예측
def prediction_crops_prod(request):
    return render(request, 'prediction_crops_prod.html')

# crops_trend.html, 지역별 작물 트렌드
def crops_trend(request):
    return render(request, 'crops_trend.html')



# climate 기상정보 input : 지역, output : 년도별 추이
# pord_info 농작물 생산정보 input : 작물 + 지역, output : 면적당 생산량
# prod_change 농작물 생산량 변화 input : 작물, output : 년도별 생산량 흐름 (전년대비 증감율)
# growing_period 농작물 생육기간 input : , output : 생육 기간 테이블
# going_north 농작물 북상 input : 작물, output : 재배 가능지 + 추가된 지역
# crops_trend 지역별 작물 트렌드 input : 지역, output : 해당지역의 생산량 pie chart(최근 5년)
# crops_map 농작물 map input : 지역 + 작물, output : 지도 위 작물 생산량 (최근 5년)


# prediction_prod 농작물 생산성 예측 input : 지역 + 면적, output : 생산량 + 작물 예측
class Predict(views.APIView):
    @csrf_exempt
    def post(self, request):
        # "local": ['지역명'], 'area': ['면적 ha']
        request_dict = dict(request.POST)

        local = request_dict['option1'][0]

        predict_prod = CropsConfig.predict_prod
        predict_prod_per_area = CropsConfig.predict_prod_per_area

        crops_prod = dict()
        
        if local == "전국":
            for crop, area_prod in predict_prod.items():
                sum = 0
                for value in area_prod.values():
                    if value > 0:
                        sum += value
                crop_name = crop.split("_")

                if crop_name[1] == "-":
                    crop_name = crop_name[0]
                else:
                    crop_name = crop_name[1] + " " + crop_name[0]
                crops_prod[crop_name] = sum
        else:
            for crop, area_prod in predict_prod.items():
                if local in area_prod.keys():
                    if area_prod[local] > 0:
                        crop_name = crop.split("_")

                        if crop_name[1] == "-":
                            crop_name = crop_name[0]
                        else:
                            crop_name = crop_name[1] + " " + crop_name[0]
                        crops_prod[crop_name] = area_prod[local]
        print(crops_prod)

        for key, value in list(crops_prod.items()):  ## list , items를 꼭 써야함.
            if value < 0:
                del crops_prod[key]

        crops_prod = sorted(crops_prod.items(), key=lambda x: x[1], reverse=True)

        data = dict()
        for i in crops_prod:
            data[i[0]] = i[1]

        result = json.dumps(data)
        return render(request, "prediction_prod.html", {'result': result})


# prediction_prod 농작물 생산성 예측 input : 지역 + 면적, output : 생산량 + 작물 예측
class Predict_crop(views.APIView):
    @csrf_exempt
    def post(self, request):
        request_dict = dict(request.POST)

        crop = request_dict['option1'][0]

        crop = crop.split(" ")

        if len(crop) > 1:
            crop = crop[1] + "_" + crop[0]
        else:
            crop = crop[0] + "_-"

        predict_prod = CropsConfig.predict_prod

        crops_prod = predict_prod[crop]

        for key, value in list(crops_prod.items()):  ## list , items를 꼭 써야함.
            if value < 0:
                del crops_prod[key]

        crops_prod = sorted(crops_prod.items(), key=lambda x: x[1], reverse=True)

        data = dict()
        for i in crops_prod:
            data[i[0]] = i[1]

        print(data)
        result = json.dumps(data)
        return render(request, "prediction_crops_prod.html", {'result': result})


# Trend 지역별 생산량 정보
class Trend(views.APIView):
    @csrf_exempt
    def post(self, request):

        request_dict = dict(request.POST)

        area = request_dict['option1'][0]

        crop_list = {
            "GamgulProdArea": "감귤", "PotatoFallProdArea": "가을 감자", "PotatoHighlandProdArea": "고랭지 감자",
            "PotatoSpringProdArea": "봄 감자", "ChiliProdArea": "고추", "DangamProdArea":"단감", "CarrotProdArea": "당근",
            "LargeonionProdArea": "대파", "PeanutProdArea":"땅콩", "GarlicProdArea":"마늘", "DaikonFallProdArea":"가을 무",
            "DaikonHighlandProdArea":"고랭지 무", "DaikonSpringProdArea":"봄 무", "DaikonWinterProdArea": "무_겨울",
            "PearProdArea":"배", "NapacabbageWinterProdArea":"겨울 배추", "NapacabbageHighlandProdArea":"고랭지 배추",
            "NapacabbageSpringProdArea":"봄 배추", "PeachProdArea":"복숭아", "AppleProdArea": "사과", "GingerProdArea":"생강",
            "SpinachProdArea":"시금치","CabbageProdArea": "양배추", "OnionProdArea":"양파", "ChivesProdArea":"쪽파",
            "SesameProdArea":"참깨", "GrapeProdArea":"포도", "NapacabbageFallProdArea": "가을 배추"
        }

        # 면적, 생산량 정보
        data = dict()
        if area == "전국":
            for table, crop in crop_list.items():
                table_data = getattr(models, table).objects.all().values()
                table_df = pd.DataFrame(list(table_data))

                crops_prod = table_df[table_df["year"] == 2020].sum()["prod"]

                data[crop] = int(crops_prod)
        else:
            for table, crop in crop_list.items():
                table_data = getattr(models, table).objects.all().values()
                table_df = pd.DataFrame(list(table_data))

                crops_prod = table_df[(table_df["year"] == 2020) & (table_df["region"] == area)].sum()["prod"]

                data[crop] = int(crops_prod)

        data = sorted(data.items(), key=lambda x: x[1], reverse=True)
        print(data)

        new_data = dict()
        for i in data:
            new_data[i[0]] = i[1]

        result = json.dumps(new_data)
        return render(request, "crops_trend.html", {'result': result})


class Change(views.APIView):
    @csrf_exempt
    def post(self, request):

        request_dict = dict(request.POST)

        crop = request_dict['option1'][0]

        crop_list = {
            "GamgulProdArea": "감귤", "PotatoFallProdArea": "가을 감자", "PotatoHighlandProdArea": "고랭지 감자",
            "PotatoSpringProdArea": "봄 감자", "ChiliProdArea": "고추", "DangamProdArea":"단감", "CarrotProdArea": "당근",
            "LargeonionProdArea": "대파", "PeanutProdArea":"땅콩", "GarlicProdArea":"마늘", "DaikonFallProdArea":"가을 무",
            "DaikonHighlandProdArea":"고랭지 무", "DaikonSpringProdArea":"봄 무", "DaikonWinterProdArea": "무_겨울",
            "PearProdArea":"배", "NapacabbageWinterProdArea":"겨울 배추", "NapacabbageHighlandProdArea":"고랭지 배추",
            "NapacabbageSpringProdArea":"봄 배추", "PeachProdArea":"복숭아", "AppleProdArea": "사과", "GingerProdArea":"생강",
            "SpinachProdArea":"시금치","CabbageProdArea": "양배추", "OnionProdArea":"양파", "ChivesProdArea":"쪽파",
            "SesameProdArea":"참깨", "GrapeProdArea":"포도", "NapacabbageFallProdArea": "가을 배추"
        }

        # 면적, 생산량 정보
        data = dict()
        for table, crop_name in crop_list.items():
            if crop_name == crop:
                table_data = getattr(models, table).objects.all().values()
                table_df = pd.DataFrame(list(table_data))

                for year in range(2001, 2021):

                    row = [year]

                    for local in ['경기도', '강원도', '충청북도', '충청남도', '전라북도', '전라남도', '경상북도', '경상남도', '제주도']:
                        value = table_df[(table_df["region"] == local) & (table_df["year"] == year)]["prod"]
                        print(value)
                        if value.empty:
                            value = 0
                        else:
                            value = value[0]

                        print(type(row))
                        row = row.append(value)

                    data[year] = row
        print(data)
        result = json.dumps(data)
        return render(request, "crops_change.html", {'result': result})



class ResultAPIView(views.APIView):
    def post(self, request):
        result = request.POST
        print(result)
        data = "hi"
        context = {
            'result': result
        }
        json_data = json.dumps(context)
        return render(request, "climate.html", {'result': json_data})

