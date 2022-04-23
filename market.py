from flask import Flask

app = Flask(__name__)

#from app import routes
@app.route('/')
def henlo_world():
    return "<h1>Henlo World!</h1>"
