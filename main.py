import speech_recognition as  sr
import pyttsx3 
import pywhatkit
import datetime
import json
import os 
import wikipedia

settings = 'settings.json'

if(os.path.exists(settings)):
    print("ok")
else:
    data ={
        'lang':'en'
    }
    with open(settings,'w') as f:
        json.dump(data,f)


listener =  sr.Recognizer()
engine  = pyttsx3.init()

def talk(text):
    engine.say(text)
    engine.runAndWait()




def take_command():
    try:
     with sr.Microphone() as source:
        print('listening')
        voice= listener.listen(source)
        command = listener.recognize_google(voice)
        command = command.lower()
        if 'alexa'  in command:
                command = command.replace('alexa','')

    except:
        pass
    return command

def run_alexa():
    command = take_command()
    if  'play' in command:
        song = command.replace('play', '')
        talk('playing ' + song)
        pywhatkit.playonyt(song)
    if 'time'  in command:
        time = datetime.datetime.now().strftime('%H:%M')
        talk('Current time is' + time)
    
    if 'who' in command:
        person = command.replace('who is','')
        info= wikipedia.summary(person,1)
        print(info)
        talk(info)

run_alexa()