import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def talk(text):
    engine.say(text)
    engine.runAndWait()

def speak():
    try:
        with sr.Microphone() as mic:
            print('I\'m listening')
            voice = listener.listen(mic)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'jarvis' in command:
                command = command.replace('jarvis', '')
                return command

    except NameError:
        talk('I couldn\'t hear you')
        print(NameError)

print(speak())