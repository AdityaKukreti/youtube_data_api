from youtubeAPI import *
from notesAPI import *
from flask import Flask,jsonify,request

UPLOAD_FOLDER = 'uploads/'
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

youtubeAPI = YoutubeAPI()
notesAPI = NotesGenerator()

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
    


@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return 'No file uploaded', 400

    file = request.files['file']

    if file.filename == '':
        return 'No file selected', 400

    file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
    file.save(file_path)

    return 'File uploaded successfully', 200
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
