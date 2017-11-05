from flask import Flask, render_template, request, jsonify, abort, redirect, url_for
from flask_cors import CORS
import os, json, time
# from clarifai.rest import ClarifaiApp
# from clarifai.rest import Image as ClImage

# clarifai_app = ClarifaiApp(api_key='')

app = Flask(__name__)
CORS(app)

UPLOAD_FOLDER = 'static/uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

DB = {
    1 : {
        'name': 'Bella',
        'color': 'black',
        'description': 'none',
        'spayed_neutured': 'unknown',
        'feral_domestic': 'unknown',
        'points': [
            {'image':'angry.jpg','latlng': (43.003158, -78.787532), 'timestamp': 1509768000,'desc':''},
            {'image':'angry.jpg','latlng': (43.004028, -78.785915), 'timestamp': 1509796800,'desc':''}
        ]},
    2 : {
        'name': 'Sam',
        'color': 'Silver w Black stripes',
        'description': 'none',
        'spayed_neutured': 'unknown',
        'feral_domestic': 'unknown',
        'points': [
            {'image':'j09w6p65.jpg','latlng': (43.004278, -78.789974), 'timestamp': 1509768000,'desc':''},
            {'image':'j09w6p65.jpg','latlng': (43.006263, -78.785919), 'timestamp': 1509796800,'desc':''}
        ]},
      3 : {
        'name': 'Octocat',
        'color': 'Black',
        'description': 'Somehow it looks like both a cat and an octopus',
        'spayed_neutured': 'unknown',
        'feral_domestic': 'unknown',
        'points': [
            {'image':'Octocat.png','latlng': (43.002700, -78.787421), 'timestamp': 1509768000,'desc':''},
           
        ]},  
}

#view
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/cats')
def getCats():
    return jsonify(DB)

#add cat
@app.route('/cat/add', methods=['POST'])
def addCat():
    if request.method == 'POST':
        #get cat data and insert to database
        data = json.loads(request.data)
        new_key = max(DB.keys()) + 1

        data['points'] = []
        DB[new_key] = data
        
        #return success or error message
        return jsonify(DB)
    else:
        return abort(400)

#get cat info
@app.route('/cat/<int:cat_id>')
def getCatInfo(cat_id):
    if cat_id in DB:
        return jsonify(DB[cat_id])
    else:
        return abort(404)

#add picture or location
@app.route('/cat/<int:cat_id>/add', methods=['POST'])
def addPoint(cat_id):
    if cat_id in DB and request.method == 'POST':
        #save image
        if 'image' in request.files:
            file = request.files['image']
            filename = file.filename
            f = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(f)
        else:
            filename = ''

        timestamp = time.time()
        data = request.form
        
        DB[cat_id]['points'].append({'image': filename,
                                    'latlng': (float(data['latitude']), float(data['longitude'])), 
                                    'timestamp': timestamp,
                                    'desc': data['description']})
        # return jsonify(DB[cat_id])
        return redirect(url_for('index'))
    else:
        return abort(404)


if __name__ == "__main__":
    app.run(debug = True)