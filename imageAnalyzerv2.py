# -*- coding: utf-8 -*-
"""
Created on Mon Jul 22 19:17:43 2019

@author: Andrew
"""

# Dependencies
import matplotlib.pyplot as plt

import os
import numpy as np
import tensorflow as tf

import keras
from keras.preprocessing import image
from keras.applications.vgg19 import (
    VGG19, 
    preprocess_input, 
    decode_predictions
)

# Load the VGG19 model
# https://keras.io/applications/#VGG19
model = VGG19(include_top=True, weights='imagenet')

# Define default image size for VGG19
image_size = (224, 224)

# Refactor above steps into reusable function
def predict(image_path):
    """Use VGG19 to label image"""
    img = image.load_img(image_path, target_size=image_size)
    x = image.img_to_array(img)
    x = np.expand_dims(x, axis=0)
    x = preprocess_input(x)
    predictions = model.predict(x)
    plt.imshow(img)
    return(decode_predictions(predictions, top=1))
    
#print(predict(os.path.join('static','images','webscraped','1.jpg')))

