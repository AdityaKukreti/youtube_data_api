from youtubeAPI import *
from notesAPI import *
from flask import Flask,jsonify,request

app = Flask(__name__)
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


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
