from flask import Flask
from flask import request
import ssl
import base64
import urllib 
from captcha_model_build import test
import neurallib as nl

from flask_cors import CORS

context = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)
context.load_cert_chain('cert.crt', 'privateKey.key')

app = Flask(__name__)
CORS(app)

model = nl.NN().readNNModel('temp_data.pkl')

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
  return output_str

if __name__ == "__main__":
  app.run(host= '0.0.0.0',port=80, ssl_context=context, threaded=True)
