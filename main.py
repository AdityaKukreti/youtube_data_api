from youtubeAPI import *
from flask import Flask,jsonify,request

app = Flask(__name__)
youtubeAPI = YoutubeAPI()

@app.route('/')
def initialRoute():
    return jsonify({"status":True})

@app.route('/query',methods = ['POST'])
def searchQuery():
    query = request.get_json()['query']
    youtubeAPI.query = query
    return jsonify({"response":youtubeAPI.search()})
# API_CLASS = YoutubeAPI("Flutter")

# print(API_CLASS.search())

# if __name__ == "__main__":
#     app.run(host="0.0.0.0", port=10000)
