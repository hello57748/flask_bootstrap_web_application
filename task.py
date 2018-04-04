#**********************************************************************
# task.py
# Name: Samuel Peters
# Last Modified: 3/21/18
# Course: CST 205
# Description: homework #4, Creating a web application that displays some random images and has links for all of them.
#**********************************************************************
from image_information import image_info
from flask_bootstrap import Bootstrap
from flask import Flask, render_template
import requests, json
import random
from PIL import Image

app = Flask(__name__)
bootstrap = Bootstrap(app)

#homepage
@app.route('/')
def home():

    #create random numbers
    index_1 = 0
    index_2 = 0
    index_3 = 0
    while (index_1 == index_2) or (index_1 == index_3) or (index_2 == index_3):
        index_1 = random.randint(0, 9)
        index_2 = random.randint(0, 9)
        index_3 = random.randint(0, 9)
    indecies = [index_1, index_2, index_3]

    #create filenames list
    filenames = []
    for i in range(0, len(image_info)):
        filenames.append('images/' + image_info[i]['id'] + '.jpg')

    return render_template('home.html', indecies=indecies, image_info=image_info, filenames=filenames)

#image
@app.route('/picture/<image_id>')
def picture(image_id):

    im = Image.open('static/images/' + image_id + '.jpg')
    sizes = im.size
    mode = im.mode
    format = im.format

    return render_template('image.html', image_id=image_id, image_info=image_info, sizes=sizes, mode=mode, format=format)

"""
3 STEPS TO RUN:
    export FLASK_APP=task.py
    export FLASK_DEBUG=1
    flask run
"""
