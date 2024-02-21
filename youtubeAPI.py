from googleapiclient.discovery import build
import os


class YoutubeAPI:

    def __init__(self) :
        self.api_key = os.environ["YOUTUBE_API_KEY"]
        self.youtube = build('youtube', 'v3', developerKey=self.api_key)
        self.query = ""
    
    def search(self):
        request = self.youtube.search().list(
            q = self.query,
            part = 'snippet',
            maxResults = 10
        )
        response = request.execute()
        vidNo = 1
        result = {}
        for i in response['items']:
            content = {}
            if (i['id']['kind'] == "youtube#video"):
                for j in i:
                    if (j == 'snippet' or j == "id"):
                        content[j] = i[j]
                result[vidNo] = content
                vidNo += 1

        return result
