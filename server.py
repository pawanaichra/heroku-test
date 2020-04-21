import base64
from flask import Flask
from flask import request
app = Flask(__name__)

@app.route("/")
def root():
  try:
    print("hello")
  except Exception as err:
    print(err)
  return "done"
app.run()
