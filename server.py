from flask import Flask
from flask import request
import ssl
import base64
import urllib 
from captcha_model_build import test
import neurallib as nl


app = Flask(__name__)

model = nl.NN().readNNModel('temp_data.pkl')

@app.route("/")
def homePage():
  return "Captcha hosted : make /predict call"

@app.route("/predict")
def predict():
  url_encoded_string = request.args.get('captchaString')
  #print("Obtained argument \n" , url_encoded_string)
  decoded_string = urllib.parse.unquote(url_encoded_string) 
  png_data = decoded_string.split(',')
  #print(png_data[1])
  with open("tmp_img.png", "wb") as fh:
    fh.write(base64.b64decode(png_data[1]))
  output_str = test(model,"tmp_img.png")
  print("========= Output Value ========= : ", output_str)
  return output_str

if __name__ == "__main__":
  app.run(host='0.0.0.0',port=8010)
