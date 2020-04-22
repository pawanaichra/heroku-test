import base64
from flask import Flask
from flask import request
import numpy as np
from PIL import Image
import cv2
from app.logistic import logistic_func
  
app = Flask(__name__) 
  
@app.route("/", methods=['POST'])
def root():
  try:
    imgstring = request.form['image']
    imgdata = base64.b64decode(imgstring)
    image = Image.open(io.BytesIO(imgdata))
    rgb = cv2.cvtColor(np.array(image), cv2.COLOR_BGR2RGB)
    result = logistic_func(rgb)
#     with open("img.jpg", 'wb') as f:
#       f.write(imgdata)
    return result
  except Exception as err:
    print(err)
