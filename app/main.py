import base64
from flask import Flask
from flask import request
from app.logistic import logistic_func
  
app = Flask(__name__) 
  
@app.route("/", methods=['POST'])
def root():
  try:
    imgstring = request.form['image']
    imgdata = base64.b64decode(imgstring)
    result = logistic_func(imgdata)
#     with open("img.jpg", 'wb') as f:
#       f.write(imgdata)
    return result
  except Exception as err:
    print(err)
