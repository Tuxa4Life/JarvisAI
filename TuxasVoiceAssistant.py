import speech_recognition as sr
import pyttsx3

class VoiceAssistant():
    def __init__(self):
        self.listener = sr.Recognizer()
        self.engine = pyttsx3.init()


    def talk(self, text):
        self.engine.say(text)
        self.engine.runAndWait()


    def command(self):
        with sr.Microphone() as source:
            self.talk('Listening')

            audio = self.listener.listen(source)
            try:
                command = self.listener.recognize_google(audio)
                command = command.lower()

                self.talk('Got it')
                if 'nothing' in command or 'cancel' in command:
                    return ' '
                return command
            except:
                self.talk("Couldn't hear you well")

# dummy
def main():
    vs = VoiceAssistant()

    vs.talk('Hello im Nick\'s voice assistant.')
    print(vs.command())

if __name__ == "__main__":
    main()