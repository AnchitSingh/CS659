#! /usr/bin/python3
# AUM SHREEGANESHAAYA NAMAH||
import os
from flask import Flask, request
from label import getLabel

app = Flask(__name__)
# app.config.from_object(os.environ['APP_SETTINGS'])
# app.config['UPLOAD_FOLDER'] = "./tmp"

@app.route('/')
def hello():
    return "Hello World!"

@app.route('/upload', methods=["POST"])
def upload_file():
    print(request.files['media'])
    f = request.files['media']
    f.save(f"save_{f.filename}")
    maxLabel, outCome = getLabel(f"save_{f.filename}")
    os.remove(f"save_{f.filename}")
    return f"{maxLabel}|{outCome}"

#@app.route('/<name>')
#def hello_name(name):
#    return f"Hello {name}!"

if __name__ == '__main__':
    app.run(host="0.0.0.0")
