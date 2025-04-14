from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Shopping list  soon.. on other site!'
