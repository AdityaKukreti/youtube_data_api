# import requests

# url = "http://127.0.0.1:10000/query"
# request = requests.post(url,json={'query':"flutterrrrr"})
# print(request.json())

# url = "https://atman.onrender.com/random-questions"
# request = requests.get(url=url)
# print(request)

from youtube_transcript_api import YouTubeTranscriptApi
from openai import OpenAI
import os

# transcription = ""
# for i in YouTubeTranscriptApi.get_transcript("vBURTt97EkA"):
#     transcription += i['text'] + ' '

# transcription.replace('\n',' ')
# # print(transcription)


# client = OpenAI(api_key=os.environ['OPENAI_API_KEY'])

# stream = client.chat.completions.create(
#     model="gpt-3.5-turbo",
#     messages=[{"role":"system", "content":'''Task: Write detailed notes with necessary terms from video transcriptions, translating from any language to English, using proper headings and subheadings.

# Instructions:

# Provide a summary of the video content.
# Use proper headings and subheadings to organize the notes.
# Include necessary terms and concepts mentioned in the video.
# Translate any non-English content into English.
# Ensure the total character count does not exceed 16,000 characters.
# Additional Information:

# The notes should be comprehensive and cover all key points discussed in the video.
# Maintain clarity and coherence throughout the document.
# Use concise language and avoid unnecessary details.
# Pay attention to terminology and ensure accurate translations.
# Aim for a balanced level of detail, avoiding both excessive brevity and verbosity.
# '''},
#               {"role": "user", "content": transcription}],
#     stream=False,
# )
# # for chunk in stream:
# #     # if chunk.choices[0].delta.content is not None:
# #     #     print(chunk.choices[0].delta.content, end="")
# #     print(chunk)
# print(stream.choices[0].message.content)

class NotesGenerator:

    def __init__(self):
        self.videoId = ""
        self.transcription = ""
        self.client = OpenAI(api_key=os.environ['OPENAI_API_KEY'])

    def getTranscription(self):
        self.transcription = ""
        for i in YouTubeTranscriptApi.get_transcript(self.videoId):
            self.transcription += i['text'] + ' '
        self.transcription.replace('\n',' ')

    def generateNotes(self):
        self.getTranscription()
        stream = self.client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role":"system", "content":'''Task: Write detailed notes with necessary terms from video transcriptions, translating from any language to English, using proper headings and subheadings.

        Instructions:

        Provide a summary of the video content.
        Use proper headings and subheadings to organize the notes.
        Add <h> and <s> before and after the heading and sub-headings respectively.
        Provide atleast 1 extra detailed example for each topic.
        Include necessary terms and concepts mentioned in the video.
        Translate any non-English content into English.
        Ensure the total character count does not exceed 16,000 characters.
        Additional Information:

        The notes should be comprehensive and cover all key points discussed in the video.
        Maintain clarity and coherence throughout the document.
        Use concise language and avoid unnecessary details.
        Pay attention to terminology and ensure accurate translations.
        Aim for a balanced level of detail, avoiding both excessive brevity and verbosity.
        '''},
                {"role": "user", "content": self.transcription}],
        stream=False,
        )

        return stream.choices[0].message.content

    

