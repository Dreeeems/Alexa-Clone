import speech_recognition as  sr
import pyttsx3 
import datetime
import json
import os 
import wikipedia
import commands
from functions import playing, va_change_lang
from changeLang import recognize_speech
settings = 'settings.json'






def init():
    if(os.path.exists(settings)):
        with open(settings, 'r') as file:
            data = json.load(file)
            recognize_speech(data["lang"])
            return 
 
    else:
        data ={
        'lang':'EN-US',
        'num':'1'
            }
    with open(settings,'w') as f:
        json.dump(data,f)
    with open(settings, 'r') as file:
        data = json.load(file)
        recognize_speech(data["lang"])
        return 
    

listener =  sr.Recognizer()
engine  = pyttsx3.init()
voices = engine.getProperty('voices')




def talk(text):
    
    with open(settings, 'r') as file:
        data = json.load(file)
        voiceId = data['lang']
        for voice in voices:
            if voiceId in voice.id:
                voiceId = voice.id
                engine.setProperty("voice",voiceId)
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
      
        if command == None:
            command=""
    except:
        command=""
    return command

def run_alexa():
    settingFile = init()
    command = take_command()
    print(command)
    if  'play' in command:
        playing(command,talk)
    if 'time'  in command:
        time = datetime.datetime.now().strftime('%H:%M')
        talk('Current time is' + time)
    
    if 'who' in command:
        person = command.replace('who is','')
        info= wikipedia.summary(person,1)
        talk(info)
    if 'change' in command:
       lang = va_change_lang(command)
       print(lang)
       talk("The new language will be" + str(lang[2]))
       recognize_speech(lang[0])
       with open(settings, "w") as f:
        data={
            'lang':lang[0],
            'num':lang[1],
            'name':lang[2]
        }
        json.dump(data, f)



       



       talk('New language is ' + lang[2]) 
    else:
        talk(command)
        return 


run_alexa()