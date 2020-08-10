import flask
from flask import request, jsonify, redirect, url_for
import json

from models.fronton import Fronton
from controllers.frontones_controller import FrontonesController


app = flask.Flask(__name__)
app.config["DEBUG"] = True


#APIs calls
frontones_controller = FrontonesController()




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
        user=request.form.get('user')
        
        print("lat:%s lon:%s user: %s"%(lat,lon,user))
        frontones_controller.check_pick_and_write_fronton_to_json(lat,lon,fronton_index,user)
        return redirect(url_for('frontones'))
    else:
        all_frontones = frontones_controller.get_frontones_from_JSON()
        #wanted = next(f if f.index == fronton_index else 'None' for f in all_frontones)
        try:
            #wanted = next(f if str(f.index) == str(fronton_index) else 'None' for f in all_frontones)
            # @MD change this to upper line
            for f in all_frontones:
                if f.index == fronton_index:
                    wanted=f
            print(fronton_index)
            print(wanted)
            return jsonify(wanted.as_dict())
        except Exception:
            return jsonify('an error ocurred dude')



app.run(port=8080)
