from flask import Flask
import os

app = Flask(__name__)

name = os.environ['name']


@app.route('/dockerdemo')
def dockerdemo():
    return name + " welcome to my container!"


if (__name__) == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=True)
