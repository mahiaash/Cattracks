from flask import Flask, render_template, request, jsonify, abort
import os, requests, json
# from clarifai.rest import ClarifaiApp
# from clarifai.rest import Image as ClImage

# clarifai_app = ClarifaiApp(api_key='')

app = Flask(__name__)

UPLOAD_FOLDER = os.path.basename('uploads')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

#view
@app.route('/')
def hello_world():
    return render_template('index.html')

#add cat
@app.route('/addcat', methods=['POST'])
def addCat():
    if request.method == 'POST':
        #get cat data and insert to database
        
        #return success or error message
        return jsonify()
    else:
        return abort(400)

#add cat location
@app.route('/<cat_id>')
def addPlaceImage(cat_id):
    if request.method == 'POST':
        data = request.form
        #get location data 

        #if there is an image file add image 

        #insert into database

        #return success or error message
        return jsonify({})
    else:
        return abort(400)


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