import speech_recognition as sr
import pyttsx3
import datetime
import pywhatkit
import wikipedia
import pyjokes

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def defCommand(value):
    talk('u said: ' + value)

def talk(text):
    engine.say(text)
    engine.runAndWait()

with sr.Microphone() as source:
    print('listening')
    while True:
        audio = listener.listen(source)
        try:
            command = listener.recognize_google(audio)
            command = command.lower()

            print(command)

        except:
            print("Couldn't hear you well")