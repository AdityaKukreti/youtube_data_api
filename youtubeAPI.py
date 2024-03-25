# from googleapiclient.discovery import build
# import os


# class YoutubeAPI:

#     def __init__(self):
#         self.api_key = os.environ["YOUTUBE_API_KEY"]
#         self.youtube = build('youtube', 'v3', developerKey=self.api_key)
#         self.query = ""
    
#     def get_channel_thumbnail(self,channel_id):
#         request = self.youtube.channels().list(
#         part='snippet',
#         id=channel_id
#         )
#         response = request.execute()
#         if response.get('items'):
#             thumbnail_url = response['items'][0]['snippet']['thumbnails']['default']['url']
#             return thumbnail_url

#     def statistics(self, id):
#         statistics_request = self.youtube.videos().list(
#             part="statistics",
#             id = id
#         )
#         statistics_response = statistics_request.execute()
#         return statistics_response
#     # def search(self):
#     #     request = self.youtube.search().list(
#     #         q = self.query,
#     #         part = 'snippet',
#     #         maxResults = 20,
#     #         type='video',
#     #         videoCategoryId = '27'
#     #     )
#     #     response = request.execute()
#     #     result = {}
#     #     vidNo = 1
#     #     for i in response.get('items'):
           
#     #         content = {}
#     #         # if (i['id']['kind'] == "youtube#video"):
#     #         title = i['snippet']['title'].lower()
#     #         description = i['snippet']['description'].lower()
#     #         if ('tutorial' in title or 'tutorial' in description or 'lesson' in title or 'lesson' in description or 'learn' in title or 'learn' in description or 'educational' in title or 'educational' in description):
            
#     #             content['id'] = i['id']
#     #             content['snippet'] = i['snippet']
#     #             content['items'] = self.statistics(i['id']['videoId'])['items']
#     #             content['channel_thumbnail'] = self.get_channel_thumbnail(i['snippet']['channelId'])
                
#     #             result[vidNo] = content
#     #             vidNo += 1
#     #     return result
#     def search(self):
#         request = self.youtube.search().list(
#             q=self.query,
#             part='snippet',
#             maxResults=20,
#             type='video',
#             videoCategoryId='27'
#         )
#         response = request.execute()
#         result = {}
#         vidNo = 1
    
#         # First, get the video IDs from the search results
#         video_ids = []
#         for search_result in response.get('items', []):
#             if search_result['id']['kind'] == 'youtube#video':
#                 video_ids.append(search_result['id']['videoId'])
    
#         # Fetch the full video details, including the full description
#         video_details_response = self.youtube.videos().list(
#             id=','.join(video_ids),
#             part='snippet,contentDetails,statistics'
#         ).execute()
    
#         # Process the video details
#         for video_detail in video_details_response.get('items', []):
#             content = {}
#             title = video_detail['snippet']['title'].lower()
#             description = video_detail['snippet']['description'].lower()
    
#             # Overwrite the description with the full description from contentDetails
#             content['snippet'] = video_detail['snippet']
#             # try:
#             # content['snippet']['description'] = video_detail['contentDetails']['description']
#             print(content['snippet']['description'], end = '\n\n\n')
            
#             # except:
#                 # print(content['snippet']['description'])
#                 # print()
#                 # print(video_detail)
            
#             if ('tutorial' in title or 'tutorial' in description or
#                 'lesson' in title or 'lesson' in description or
#                 'learn' in title or 'learn' in description or
#                 'educational' in title or 'educational' in description):
#                 content['id'] = video_detail['id']
#                 content['items'] = video_detail['statistics']
#                 content['channel_thumbnail'] = self.get_channel_thumbnail(video_detail['snippet']['channelId'])
#                 result[vidNo] = content
#                 vidNo += 1
    
#         return result
    
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
            title = i['snippet']['title'].lower()
            description = i['snippet']['description'].lower()
           
            if ('course' in title or 'course' in description or 'tutorial' in title or 'tutorial' in description or 'lesson' in title or 'lesson' in description or 'learn' in title or 'learn' in description or 'educational' in title or 'educational' in description or 'note' in title or 'note' in description):
            
                content['id'] = i['id']
                content['snippet'] = i['snippet']
                content['items'] = self.statistics(i['id']['videoId'])['items']
                content['channel_thumbnail'] = self.get_channel_thumbnail(i['snippet']['channelId'])
              
                result[vidNo] = content
                vidNo += 1
        return result
    
