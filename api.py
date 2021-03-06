import flask
from flask import request, jsonify, redirect, url_for
import json

from models.fronton import Fronton
from controllers.frontones_controller import FrontonesController


app = flask.Flask(__name__)
app.config["DEBUG"] = True


#APIs calls
frontones_controller = FrontonesController()

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    return redirect(url_for("frontones"))

@app.route('/frontones/', methods=['GET'])
def frontones():
    all_frontones = frontones_controller.get_frontones_from_JSON()
    #convert to dict and jsonify
    return jsonify([fronton.__dict__ for fronton in all_frontones])

@app.route('/frontones/<fronton_index>/', methods=['GET','POST'])
def fronton_get(fronton_index:str):

    if request.method == 'POST':

        lat=request.form.get('lat')
        lon=request.form.get('lon')
        status=request.form.get('status')
        user=request.form.get('user') 
        print("lat:%s\nlon:%s\nuser:%s\nstatus:%s\n"%(lat,lon,user,status))
        if status == "1":
            print("sdfsdfsdf")
            #capturar
            operation_result=frontones_controller.check_pick_and_write_fronton_to_json(lat,lon,fronton_index,user)
            print(operation_result)
            return jsonify(operation_result)

        elif status == '0':
            print('freeing')
            operation_result=frontones_controller.free_fronton_and_write_to_json(fronton_index,user)
            return jsonify(operation_result)
        return jsonify('other')
    else:
        all_frontones = frontones_controller.get_frontones_from_JSON()
        try:
            wanted = next(( f for f in all_frontones if f.index == fronton_index),'No fronton by that index')
            return jsonify(wanted.as_dict())
        except Exception:
            return jsonify('an error ocurred dude')

            
app.run(port=8080)
