from flask import Flask
from flask import request
import ssl
import base64
import urllib 

context = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)
context.load_cert_chain('cert.crt', 'privateKey.key')

app = Flask(__name__)

@app.route("/")
def hello():
  par = request.args.get('arg')
  print("Obtained argument \n" , par)
  decoded = urllib.parse.unquote(par) 
  data = decoded.split(',')
  print(data[1])
  with open("file.png", "wb") as fh:
    fh.write(base64.b64decode(data[1]))
  return dec
 
if __name__ == "__main__":
  app.run(host= '0.0.0.0',port=80, ssl_context=context, threaded=True)
