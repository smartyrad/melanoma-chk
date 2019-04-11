from __future__ import unicode_literals

from pricecheck.config import *

# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.shortcuts import render
from django.shortcuts import render, redirect
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.shortcuts import render
from django.conf import settings
from django.core.files.storage import FileSystemStorage

#

# import tensorflow as tf
# import keras.backend.tensorflow_backend
import os
# os.environ["CUDA_VISIBLE_DEVICES"]="2"
#
# from keras.layers import Input, Dense
# from keras.models import Model
# from pricecheck.data import main, generate_data
# from keras.callbacks import ModelCheckpoint, EarlyStopping, ReduceLROnPlateau, TensorBoard
# from keras.models import model_from_json
# from keras.preprocessing import image
# from keras.preprocessing.image import ImageDataGenerator
#
# import matplotlib.pyplot as plt
# import pandas as pd
import numpy as np
#
# from sklearn import preprocessing
# from sklearn.metrics import roc_curve, auc, confusion_matrix
# import itertools
#
# import random
#
# df = pd.read_csv(DATA_CONFIG['data_folder'] + 'csv/ISIC-2017_Training_Part3_GroundTruth.csv')
# class_label=df['melanoma']
# class_id=df['image_id']
#
# data = []
# #
# # #Load model
# json_file = open(DATA_CONFIG['data_folder'] + 'weights/classification/nasnetsegmentedfullweights/classification.json', 'r')
# model_json = json_file.read()
# json_file.close()
# load_model = model_from_json(model_json)
# #Load weights into new model
# load_model.load_weights(DATA_CONFIG['data_folder'] + "weights/classification/nasnetsegmentedfullweights/classification.h5")
# print("Loaded model from disk")

# Create your views here.

print("ttest")
def pricecheck(request):
    saved = False
    if request.method == 'POST' and request.FILES['myfile']:
        print("In func")
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        print("Uploading file")
        from pathlib import Path

        my_file = Path(os.path.join(settings.MEDIA_ROOT, 'test.jpg'))
        if my_file.is_file():
            os.remove(os.path.join(settings.MEDIA_ROOT, 'test.jpg'))
        filename = fs.save('test.jpg', myfile)
        uploaded_file_url = fs.url(filename)
        saved = True
        return render(request, 'pricecheck/index.html', {
            'uploaded_file_url': uploaded_file_url
        })
    return render(request, 'pricecheck/index.html', locals())


def results(request):
    import cv2
    k = cv2.imread(os.path.join(settings.MEDIA_ROOT, 'test.jpg'))
    k = cv2.cvtColor(k, cv2.COLOR_BGR2RGB)
    k = cv2.resize(k, (331, 331))
    k = np.expand_dims(k, axis=0)
    # y_pred = load_model.predict(k)
    # classes = {'nevus': 0, 'melanoma': 1}
    # thre = 0.5
    # # obtain class predictions from probabilities
    # y_predi = (y_pred_c >= thre) * 1
    y_predi = 1
    return render(request, 'pricecheck/results.html',{'predi': y_predi})
