# from youtube_transcript_api import YouTubeTranscriptApi
# from openai import OpenAI
# import os




# class NotesGenerator:

#     def __init__(self):
#         self.client = OpenAI(api_key=os.environ['OPENAI_API_KEY'])

#     def getTranscription(self,videoId):
#         transcription = ""
#         for i in YouTubeTranscriptApi.get_transcript(videoId):
#             transcription += i['text'] + ' '
#         transcription.replace('\n',' ')
#         return transcription

#     def generateNotes(self,videoId):
#         transcription = self.getTranscription(videoId)
#         print(len(transcription.split()))
#         stream = self.client.chat.completions.create(
#         model="gpt-3.5-turbo",
#         messages=[
#             {"role":"system", "content":'''Task: Write detailed notes with necessary terms from video transcriptions, translating from any language to English, using proper headings and subheadings.

#         Instructions:

#         Provide a detailed summary of the video content.
#         Use proper headings and subheadings to organize the notes.
#         Add <h> and <s> before and after the heading and sub-headings respectively.
#         Provide atleast 1 extremely detailed example for each topic.
#         Include necessary terms and concepts mentioned in the video.
#         Translate any non-English content into English.
#            Ensure the total character count does not exceed 16,000 characters.
          
     
#         Additional Information:

#         The notes should be comprehensive and cover all key points discussed in the video.
#         Maintain clarity and coherence throughout the document.
#         Use concise language and avoid unnecessary details.
#         Pay attention to terminology and ensure accurate translations.
#         Aim for a extreme level of detail.
#         '''},
#                 {"role": "user", "content": transcription}],
#         stream=False,
#         )

#         return stream.choices[0].message.content

    
#     def generateQuiz(self,videoId):
#         stream = self.client.chat.completions.create(
#         model="gpt-3.5-turbo",
#         messages=[
#             {"role":"system", "content":'''Generate a multiple-choice quiz based on the provided video transcription. The quiz should consist of 10 questions. Each question should have a question statement and four multiple-choice options (labeled A, B, C, and D). Additionally, provide the correct answer for each question and a short explanation for the right answer.

#             Please format the output as JSON, with each question number as the key and its corresponding value containing the question statement, the four options, and the correct answer.

#             Example format:
#             {
#             "Question 1": {
#                 "Question": "What was the main topic of the video?",
#                 "Option A": "Technology",
#                 "Option B": "Science",
#                 "Option C": "History",
#                 "Option D": "Art",
#                 "Correct Answer": "A",
#                 "Explanation": "Explanation for A being the correct answer"
#             },
#             "Question 2": {
#                 "Question": "Who was the speaker in the video?",
#                 "Option A": "John",
#                 "Option B": "Emma",
#                 "Option C": "Michael",
#                 "Option D": "Sarah",
#                 "Correct Answer": "C",
#                 "Explanation": "Explanation for C being the correct answer"
#             },
#             ...
#             "Question 10": {
#                 "Question": "What was the conclusion drawn in the video?",
#                 "Option A": "A",
#                 "Option B": "B",
#                 "Option C": "C",
#                 "Option D": "D",
#                 "Correct Answer": "B",
#                 "Explanation": "Explanation for B being the correct answer"
#             }
#             }

#             Please use the provided video transcription to generate relevant questions.

#         '''},
#                 {"role": "user", "content": self.getTranscription(videoId)}],
#         stream=False,
#         )

#         return eval(stream.choices[0].message.content)
    
from youtube_transcript_api import YouTubeTranscriptApi
from openai import OpenAI
import os




class NotesGenerator:

    def __init__(self):
        self.client = OpenAI(api_key=os.environ['OPENAI_API_KEY'])

    def getTranscription(self,videoId):
        transcription = ""
        for i in YouTubeTranscriptApi.get_transcript(videoId):
            transcription += i['text'] + ' '
        transcription.replace('\n',' ')
        return transcription

    def generateNotes(self,videoId):
        transcription = self.getTranscription(videoId)
        
        
        try:
            stream = self.client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role":"system", "content":'''Task: Write detailed notes with necessary terms from video transcriptions, translating from any language to English, using proper headings and subheadings.

            Instructions:

            Provide a detailed summary of the video content.
            Use proper headings and subheadings to organize the notes.
            Add <h> and <s> before and after the heading and sub-headings respectively.
            Omit using any other tag except for <h> and <s>.
            You can add information from your end if you think the data is incomplete.
            Provide atleast 1 extremely detailed example for each topic.
            Include necessary terms and concepts mentioned in the video.
            Translate any non-English content into English.
            Ensure the total character count does not exceed 16,000 characters.
            
        
            Additional Information:

            The notes should be comprehensive and cover all key points discussed in the video.
            Maintain clarity and coherence throughout the document.
            Use concise language and avoid unnecessary details.
            Pay attention to terminology and ensure accurate translations.
            Aim for a extreme level of detail.
            '''},
                    {"role": "user", "content": transcription}],
            stream=False,
            )

            return stream.choices[0].message.content
        except:
            notes = ""
            count = len(transcription.split())
            start = 0
            print(count)
            while (start < count):
                end = 0
                if (start + 500 <= count):
                    end = start + 500
                else:
                    end = count - start
                print(start,end)
                temp_transcription = ' '.join(transcription[start:end])
                start += 500
                # stream = self.client.chat.completions.create(
                # model="gpt-3.5-turbo",
                # messages=[
                #     {
                #     "role": "system",
                #     "content": '''Generate detailed notes from lengthy video transcriptions, ensuring contextual coherence.

                # Instructions:

                # 1. Produce comprehensive summaries reflecting the video's core content.
                # 2. Organize notes using appropriate headings and subheadings.
                # 3. Utilize <h> and <s> tags to delineate headings and subheadings respectively.
                # 4. Provide at least one highly detailed example for each topic discussed.
                # 5. Incorporate pertinent terms and concepts highlighted in the transcription.
                # 6. Translate any non-English content into English for clarity.
                # 7. Ensure the total character count does not surpass 16,000 characters.

                # Additional Guidance:

                # 1. Maintain clarity and coherence throughout the notes.
                # 2. Utilize concise language, avoiding extraneous details.
                # 3. Pay meticulous attention to terminology and ensure precise translations.
                # 4. Strive for an exceptional level of detail.
                # 5. Adapt to lengthy transcriptions, with a maximum length of 10,000 words.
                # '''
                # },
                #         {"role": "user", "content": temp_transcription}],
                # stream=False,
                # )
            
                # notes += stream.choices[0].message.content + ' '
                stream = self.client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role":"system", "content":'''Task: Write detailed notes with necessary terms from video transcriptions, translating from any language to English, using proper headings and subheadings.

                Instructions:

                Provide a detailed summary of the video content.
                Use proper headings and subheadings to organize the notes.
                Add <h> and <s> before and after the heading and sub-headings respectively.
                Provide atleast 1 extremely detailed example for each topic.
                Include necessary terms and concepts mentioned in the video.
                Translate any non-English content into English.
                Ensure the total character count does not exceed 16,000 characters.
                
            
                Additional Information:

                The notes should be comprehensive and cover all key points discussed in the video.
                Maintain clarity and coherence throughout the document.
                Use concise language and avoid unnecessary details.
                Pay attention to terminology and ensure accurate translations.
                Aim for a extreme level of detail.
                '''},
                        {"role": "user", "content": temp_transcription}],
                stream=False,
                )
                notes += stream.choices[0].message.content + ' '

            return notes
    
    def generateQuiz(self,videoId):
        stream = self.client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role":"system", "content":'''Generate a multiple-choice quiz based on the provided video transcription. The quiz should consist of 10 questions. Each question should have a question statement and four multiple-choice options (labeled A, B, C, and D). Additionally, provide the correct answer for each question and a short explanation for the right answer.

            Please format the output as JSON, with each question number as the key and its corresponding value containing the question statement, the four options, and the correct answer.

            Example format:
            {
            "Question 1": {
                "Question": "What was the main topic of the video?",
                "Option A": "Technology",
                "Option B": "Science",
                "Option C": "History",
                "Option D": "Art",
                "Correct Answer": "A",
                "Explanation": "Explanation for A being the correct answer"
            },
            "Question 2": {
                "Question": "Who was the speaker in the video?",
                "Option A": "John",
                "Option B": "Emma",
                "Option C": "Michael",
                "Option D": "Sarah",
                "Correct Answer": "C",
                "Explanation": "Explanation for C being the correct answer"
            },
            ...
            "Question 10": {
                "Question": "What was the conclusion drawn in the video?",
                "Option A": "A",
                "Option B": "B",
                "Option C": "C",
                "Option D": "D",
                "Correct Answer": "B",
                "Explanation": "Explanation for B being the correct answer"
            }
            }

            Please use the provided video transcription to generate relevant questions.

        '''},
                {"role": "user", "content": self.getTranscription(videoId)}],
        stream=False,
        )

        return eval(stream.choices[0].message.content)

    def getOCRAnswer(self,text):
        stream = self.client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role":"system", "content":'''You've been provided with OCR text that requires analysis and explanation. Your task is to elucidate the meaning of the text and provide a brief explanation to aid comprehension. If the text presents a question, your response should include the answer along with a concise explanation.

Instructions:

Read the OCR text thoroughly to grasp its content.
Provide a clear and concise interpretation of the text.
Offer an explanation to aid understanding, providing any necessary context or background information.
If the text poses a question, furnish the answer along with a brief elucidation to clarify its significance.
Example OCR Text:

"Isaac Newton's law of universal gravitation states that every particle attracts every other particle in the universe with a force that is directly proportional to the product of their masses and inversely proportional to the square of the distance between their centers. F = G * (m1 * m2) / r^2."

System Response:

The OCR text discusses Isaac Newton's law of universal gravitation, which posits that all particles in the universe exert an attractive force on each other. This force is determined by the masses of the particles involved and the distance between them. The formula, F = G * (m1 * m2) / r^2, quantifies this relationship, where F represents the force of attraction, G is the gravitational constant, m1 and m2 are the masses of the two particles, and r is the distance between their centers.

Explanation:

Isaac Newton's law of universal gravitation is a fundamental principle in physics, describing the force of attraction between objects due to gravity. It elucidates why objects fall to the ground, why the Moon orbits the Earth, and why planets revolve around the Sun. The law has profound implications for understanding celestial mechanics and has paved the way for advancements in fields such as astronomy and space exploration.

        '''},
                {"role": "user", "content": text}],
        stream=False,
        )

        return stream.choices[0].message.content
