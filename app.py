from flask import Flask
app = Flask(__name__)
@app.route('/')
def hello_world():
    return '<h1> Hello Elastic Beanstalk! This is a Docker application V1.0.</h1>'
