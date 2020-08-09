import flask
from flask import request, jsonify
import json

from models.fronton import Fronton
from controllers.frontones_controller import FrontonesController


app = flask.Flask(__name__)
app.config["DEBUG"] = True


#APIs calls
frontones_controller = FrontonesController()


@app.route('/', methods=['GET'])
def home():
    frontones = frontones_controller.get_frontones_from_JSON()
    #convert to dict and jsonify
    return jsonify([fronton.__dict__ for fronton in frontones])

@app.route('/fronton/<fronton_index>', methods=['GET'])
def fronton(fronton_index):
    frontones = frontones_controller.get_frontones_from_JSON()
    wanted = "No fronton by that id duuuuuuuude"
    for f in frontones:
        if f.index == fronton_index:
            print(f.title)
            wanted = f
    return jsonify(wanted.as_dict())

@app.route('/frontones', methods=['GET','POST'])
def frontones():
    return "not ready yet :("


app.run(port=8080)
