#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct  2 00:22:10 2020

@author: tumin
"""

import numpy as np
import streamlit as st
import tensorflow as tf
from PIL import Image, ImageOps
import os
import base64
import requests
from io import BytesIO

def import_and_predict(image_data, model):
    
        size = (128,128)    
        image = ImageOps.fit(image_data, size, Image.ANTIALIAS)
        image = image.convert('RGB')
        image = np.asarray(image)
        image = (image.astype(np.float32) / 255.0)

        img_reshape = image[np.newaxis,...]

        prediction = model.predict_classes(img_reshape)
        prob = model.predict_proba(img_reshape)
        return prediction, prob

def predict(image):
    model = tf.keras.models.load_model('model.hdf5')
    prediction, prob = import_and_predict(image, model)
    
    if prediction[0,0] == 0:
        st.write("Covid-19")
        st.write("Accuray : {:.2f}".format(((1-prob[0,0]))*100),"%")
    else:
        st.write("Normal")
        st.write("Accuracy : {:.2f}".format((prob[0,0])*100),"%")

    st.image(image, use_column_width=True)


def main():
    st.sidebar.write("""
        # Covid-19 Detection using Deep Learning
        """
        )
    st.sidebar.info("Enter the Url of the X-ray, and our app will do the magic 🧙‍♂️")
    st.subheader("Enter Url and Predict")
    st.info("Our model has an accuracy of 94%")

    st.set_option('deprecation.showfileUploaderEncoding', False)

    path = st.text_input('Enter Image URL to Classify.. ','https://upload.wikimedia.org/wikipedia/commons/thumb/c/c8/Chest_Xray_PA_3-8-2010.png/947px-Chest_Xray_PA_3-8-2010.png')

    if(path != ''):
        if st.button("Predict"):        
            content = requests.get(path).content
            image = Image.open(BytesIO(content))
            predict(image)
    else:
        st.text("Enter the Url and Press ENTER")


if __name__ == "__main__":
    main()

