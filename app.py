

import json
from flask import Flask, render_template
#from flask_sqlalchemy import 

with open("./templates/data.json","r") as f:
    data=json.load(f)

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('data.json')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')