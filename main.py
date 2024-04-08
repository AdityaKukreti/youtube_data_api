from youtubeAPI import *
from notesAPI import *
from ocr import OCR
from flask import Flask,jsonify,request
import os


os.mkdir('uploads')
UPLOAD_FOLDER = 'uploads/'
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

youtubeAPI = YoutubeAPI()
notesAPI = NotesGenerator()
ocr = OCR()

@app.route('/')
def initialRoute():
    return jsonify({"status":True})

@app.route('/query',methods = ['POST'])
def searchQuery():
    query = request.get_json()['query']
    youtubeAPI.query = query
    return jsonify({"response":youtubeAPI.search()})

@app.route('/notes',methods = ['POST'])
def generateNotes():
    videoId = request.get_json()['videoId']
    try:
        return jsonify({"status":'true',"notes":notesAPI.generateNotes(videoId)})
    except:
        return jsonify({'status':'false'})
    
@app.route('/videoDetails', methods = ['POST'])
def getVideoDetails():
    videoId = request.get_json()['videoId']
    try:
        return jsonify({'status':'true','data':youtubeAPI.getVideoDetails(videoId)})
    except:
        return jsonify({'status':'false'})
    
@app.route('/generateQuiz', methods = ['POST'])
def generateQuiz():
    videoId = request.get_json()['videoId']
    try:
        return jsonify({'status':'true','data':notesAPI.generateQuiz(videoId)})
    except:
        return jsonify({'status':'false'})
    


@app.route('/chat', methods=['POST'])
def upload_file():

    print(request.get_json())

    ocrText = ""
    userText = ""
    if 'file' in request.files:
        # File is uploaded
        file = request.files['file']
        print(file.filename)

        if file.filename != '':
            # If a file is provided, save it
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
            file.save(file_path)
            ocrText = ocr.detect_text(file_path)[0]
       

    if 'text' in request.form:
        # If text is provided in the form data, use it
        userText = request.form['text']

    print(userText,ocrText)

    # Process the combined text here

    return jsonify({'text': notesAPI.getOCRAnswer(ocrText,userText)}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
