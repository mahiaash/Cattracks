from flask import Flask, render_template, request, jsonify, abort
from flask_cors import CORS
import os, json
# from clarifai.rest import ClarifaiApp
# from clarifai.rest import Image as ClImage

# clarifai_app = ClarifaiApp(api_key='')

app = Flask(__name__)
CORS(app)

UPLOAD_FOLDER = os.path.basename('uploads')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

DB = {
    1 : {
        'name': 'Bella',
        'color': 'black',
        'desc': 'none',
        'spray/neut': 'unknown',
        'feral/domestic': 'unknown',
        'points': [
            {'image':'angry.jpg','latlng': (43.003158, -78.787532), 'timestamp': 1509768000,'desc':''},
            {'image':'angry.jpg','latlng': (43.004028, -78.785915), 'timestamp': 1509796800,'desc':''}
        ]},
    2 : {
        'name': 'Sam',
        'color': 'black w brown',
        'desc': 'none',
        'spray/neut': 'unknown',
        'feral/domestic': 'unknown',
        'points': [
            {'image':'angry.jpg','latlng': (43.004278, -78.789974), 'timestamp': 1509768000,'desc':''},
            {'image':'angry.jpg','latlng': (43.006263, -78.785919), 'timestamp': 1509796800,'desc':''}
        ]},
}

#description
@app.route('/description')
def desc():
    return render_template('description.html')
#view
@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/cats')
def getCats():
    return jsonify(DB)


#add cat
@app.route('/cat/add', methods=['POST'])
def addCat():
    if request.method == 'POST':
        #get cat data and insert to database
        data = request.form
        print(request.form)
        # new_key = max(DB.keys()) + 1
        # DB[new_key] = data
        
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



#upload image example from https://stackoverflow.com/questions/28982974/flask-restful-upload-image
@app.route('/upload', methods=['POST'])
def upload_file():
    file = request.files['image']
    f = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
    
    # add your custom code to check that the uploaded file is a valid image and not a malicious file (out-of-scope for this post)

    file.save(f)

    #check, if there is a cat in the photo
    # model = app.models.get('general-v1.3')
    # image = ClImage(file_obj=open('/home/user/image.jpeg', 'rb'))
    # model.predict([image])

    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug = True)