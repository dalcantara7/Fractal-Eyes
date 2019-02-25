# -*- coding: utf-8 -*-
"""
Created on Thu Jan 24 15:10:54 2019

@author: andrew burger
"""

from keras.layers import Dense, Dropout, Flatten, Activation
from keras.layers.convolutional import Conv2D, MaxPooling2D
from keras.models import Sequential, load_model
import pandas as pd
from keras.utils import np_utils
import numpy as np
from keras.preprocessing.image import ImageDataGenerator, array_to_img, img_to_array, load_img
from PIL import Image
from keras import backend as K


"""
The input to this function a jpeg image from the given Black vs Bloodimage dataset. The filepath 
is a raw string.
for example filepath = r'C:\x86\Hello.jpg'
"""
def predicter(filepath):

    model = load_model('ECE498B.model')
    image_test = load_img(filepath, target_size = (150,150))
    image_test_array = img_to_array(image_test)
    image_test_array = np.expand_dims(image_test_array,axis=0)


    prediction = model.predict_classes(image_test_array)
    
    return prediction

