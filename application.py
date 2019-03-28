from flask import Flask
from flask_cors import CORS
from googletrans import Translator
from flask import request


app = Flask(__name__)
CORS(app)
translator = Translator()



@app.route("/")
def hello():
    translations = translator.translate(request.args['text'], dest=request.args['dest'])
    return (translations.text)
