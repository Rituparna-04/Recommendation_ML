from django.conf.urls import url
from . import ml_model
from . import ml_predict
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

urlpatterns = [
    path('build/', ml_model.recommender_system),
    #path('predict/', ml_predict.predict_recommendations),
    ]