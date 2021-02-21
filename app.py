from __future__ import division,print_function
import numpy as np
import os
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import tensorflow as tf
global graph
graph = tf.compat.v1.get_default_graph()
from flask import Flask , request, render_template
from werkzeug.utils import secure_filename
from gevent.pywsgi import WSGIServer
app = Flask(_name_)
model = load_model("cnn3.h5")
@app.route('/')
def index():
    return render_template('base.html')
@app.route('/predict',methods = ['GET','POST'])
def upload():
    if request.method == 'POST':
        f = request.files['image']
        print("current path")
        basepath = os.path.dirname(_file_)
        print("current path", basepath)
        filepath = os.path.join(basepath,'uploads',f.filename)
        print("upload folder is ", filepath)
        f.save(filepath)
        img = image.load_img(filepath,target_size = (64,64))
        x = image.img_to_array(img)
        x = np.expand_dims(x,axis =0)
        with graph.as_default():
            preds = model.predict_classes(x)
            
            print("prediction",preds)
        index = ['yes','no']
        text = "The prediction is - " + str(index[preds[0]])
    return text
if _name_ == '_main_':
    app.run(debug = True, threaded = True)