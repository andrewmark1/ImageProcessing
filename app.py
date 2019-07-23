# -*- coding: utf-8 -*-
"""
Created on Sat Jul 20 21:26:19 2019

@author: Andrew
"""

import os
from flask import (
    Flask,
    render_template,
    jsonify,
    request,
    redirect)

#import pymongo
#import json
#import googlemaps
#from bson import ObjectId, json_util
import webscrape

import os
import numpy as np
import tensorflow as tf
#import PIL
#import h5py

import keras
from keras.preprocessing import image
from keras.applications.vgg19 import (
    VGG19, 
    preprocess_input, 
    decode_predictions
)
from keras.models import load_model

import pymongo

# https://docs.mongodb.com/manual/reference/default-mongodb-port/
conn = 'mongodb+srv://andrew:gaurav@cluster0-zaofa.mongodb.net/test?retryWrites=true&w=majority'

client = pymongo.MongoClient(conn)

db = client.li
# creating collection / table
predictcollection = db.li_results
#results.drop()

#################################################
# Flask Setup
#################################################
app = Flask(__name__)

    
@app.route("/")
def home():
    
    
    return render_template("index.html")


# Query the database and send the jsonified results
@app.route("/results", methods=['GET', 'POST'])
def results():
    
    import imageAnalyzerv2

    if request.method == 'POST':
        user_search = request.form["search"]
        webscrape.webscrape(user_search)
        
#        model = VGG19(include_top=True, weights='imagenet')
#    
#        image_size = (224, 224)
#        # Load the image and resize to default image size
#        img = image.load_img("img/cute_puppies_1.jpg", target_size=image_size)
#        
#        # Preprocess image for model prediction
#        # This step handles scaling and normalization for VGG19
#        x = image.img_to_array(img)
#        x = np.expand_dims(x, axis=0)
#        x = preprocess_input(x)
        
        # Make predictions
        predictlist = []
        
        for img in os.listdir('static/images/webscraped'):    
#            print(os.path.join(user_search,img))
            predictlist.append(imageAnalyzerv2.predict(os.path.join('static','images','webscraped',img))[0][0][1])
            print(predictlist)
        
        predictdict = {predictlist[0]: 1, predictlist[1]: 1, predictlist[2]: 1}
        predictcollection.drop()
        predictcollection.insert_one(predictdict)
    
        return render_template('results.html',user_search=user_search, predict1 = predictlist[0], predict2 = predictlist[1], predict3 = predictlist[2])
    
    else:
        return render_template('results.html')
 

@app.route("/search")
def search():
        
    return render_template("search.html")

    
@app.route("/api/data")
def data():
    predictions = predictcollection.find_one({},{'_id': 0})
    
    return jsonify(predictions)


if __name__ == "__main__":
    app.run()