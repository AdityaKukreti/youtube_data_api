from googleapiclient.discovery import build
import os


class YoutubeAPI:

    def __init__(self):
        self.api_key = os.environ["YOUTUBE_API_KEY"]
        self.youtube = build('youtube', 'v3', developerKey=self.api_key)
        self.query = ""
    
    def get_channel_thumbnail(self,channel_id):
        request = self.youtube.channels().list(
        part='snippet',
        id=channel_id
        )
        response = request.execute()
        if response.get('items'):
            thumbnail_url = response['items'][0]['snippet']['thumbnails']['default']['url']
            return thumbnail_url

    def statistics(self, id):
        statistics_request = self.youtube.videos().list(
            part="statistics",
            id = id
        )
        statistics_response = statistics_request.execute()
        return statistics_response
    def search(self):
        request = self.youtube.search().list(
            q = self.query,
            part = 'snippet',
            maxResults = 20,
            type='video',
            videoCategoryId = '27'
        )
        response = request.execute()
        result = {}
        vidNo = 1
        for i in response.get('items'):
           
            content = {}
            # if (i['id']['kind'] == "youtube#video"):
            title = i['snippet']['title']
            description = i['snippet']['description']
            content['id'] = i['id']
            content['snippet'] = i['snippet']
            content['items'] = self.statistics(i['id']['videoId'])['items']
            content['channel_thumbnail'] = self.get_channel_thumbnail(i['snippet']['channelId'])
            
            result[vidNo] = content
            vidNo += 1
        return result
        

