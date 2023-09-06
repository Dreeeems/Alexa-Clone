import speech_recognition as sr
import pyttsx3
import datetime
import os
import wikipedia
import functions
listener = sr.Recognizer()
engine = pyttsx3.init()

def talk(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    try:
        with sr.Microphone() as source:
            print('Listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'alexa' in command:
                command = command.replace('alexa', '')
            return command
    except sr.UnknownValueError:
        return ""
    except sr.RequestError:
        return ""
    
def run_alexa():
    while True:
        command = take_command()
        print(command)
        if 'play' in command:
            functions.playing(command, talk)
        elif 'time' in command:
            time = datetime.datetime.now().strftime('%H:%M')
            talk('Current time is ' + time)
        elif 'who' in command:
            person = command.replace('who is', '')
            info = wikipedia.summary(person, 1)
            talk(info)
        else:
            talk(command)

if __name__ == "__main__":
    run_alexa()
