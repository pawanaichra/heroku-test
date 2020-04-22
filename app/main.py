import base64
from flask import Flask
from flask import request
  
app = Flask(__name__) 
  
@app.route("/", methods=['POST'])
def root():
  try:
    imgstring = request.form['image']
    imgdata = base64.b64decode(imgstring)
    
    with open("5.jpg", 'wb') as f:
      f.write(imgdata)
    return ("hello")
  except Exception as err:
    print(err)
