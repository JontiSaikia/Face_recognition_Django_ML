# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render , redirect,JsonResponse
import joblib
import pickle
import base64
import cv2
import pywt
#from wavelet import w2d
import util
import joblib
import json
import numpy as np

from django.views.decorators.csrf import csrf_exempt


def home(request):
    return render(request,"home.html")

def classify_image(request):
    image_data = request.form['image_data']

    response = JsonResponse(util.classify_image(image_data))

    response.headers.add('Access-Control-Allow-Origin', '*')

    return response




