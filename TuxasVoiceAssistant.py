import speech_recognition as sr
import pyttsx3
import pyautogui as pg

listener = sr.Recognizer()
engine = pyttsx3.init()

def talk(text):
    engine.say(text)
    engine.runAndWait()

def command():
    with sr.Microphone() as source:
        talk('Listening')
        while True:
            audio = listener.listen(source)
            try:
                command = listener.recognize_google(audio)
                command = command.lower()

                pg.write(command)
            except:
                talk("Couldn't hear you well")