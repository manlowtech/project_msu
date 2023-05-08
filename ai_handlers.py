import speech_recognition as sr
from gtts import gTTS
import playsound
import os
import wikipedia
"""
THIS FILE IS USED TO CONNECT OUR SYSTEM TO DIFFERENT PARTS OF
AI COMPONENTS LIKE GOOGLE TEXT TO SPEECH
IBM SPEECH TO TEXT
"""
class AiSystem:
    def __init__(self):
        pass

import pyttsx3

engine = pyttsx3.init()
voices =  engine.getProperty("voices")
engine.setProperty("voice",voices[1].id)

def talk(audio):
    engine.say(audio)
    engine.runAndWait()
def recog_audio():
    recog= sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening .....")
        audio = recog.listen(source)
    data = ""
    try:
        data = recog.recognize_google(audio)
        print("You said "+data)
    except Exception as e:
        print(e)
    return data

def response(text):
    print(text)
    tts = gTTS(text=text,lang="en")
    audio = "audio.mp3"
    tts.save(audio)
    playsound.playsound(audio)
    os.remove(audio)
def init__app():
    ai_loop = True
    while ai_loop:
        speech = recog_audio()
        #speech = "havana"
        text = ""
        try:
            if "hellos" in speech.lower():
                text = "I am good, How May I Help You"
            elif "hello" in speech.lower():
                
                # importing the module
                
                
                # finding result for the search
                # sentences = 2 refers to numbers of line
                search = speech.lower()[3:]
                text = wikipedia.summary(search, sentences = 2)
                
                # printing the result
            elif "close assistant" in speech.lower():
                break
                
            else:
                text = "Say Something, Manlow are you Ok, Would you say you are ok"
            res = response(text)
            return speech
            break
        except Exception as ex:
            print(ex)

"""
============================================================================================================
import os
import openai
openai.api_key = os.getenv("OPENAI_API_KEY")

completion = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "user", "content": "Tell the world about the ChatGPT API in the style of a pirate."}
  ]
)

print(completion.choices[0].message.content)
==============================================================================================================
import openai

content = input("User: ")
messages.append({"role": "user", "content": content})

completion = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=messages
)

chat_response = completion.choices[0].message.content
print(f'ChatGPT: {chat_response}')
"""
#talk("My Name is Manlow, I Love Mathematics. Also Delvin has a test tomorrow")