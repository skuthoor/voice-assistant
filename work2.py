import pyttsx3
import datetime
import time
import speech_recognition as sr
import webbrowser
import wikipedia
from gtts import gTTS
import os

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[2].id)
engine.setProperty('voices',voices[1].id)

def speak(audio) :
    engine.say(audio)
    engine.runAndWait()

#def tell() :
#    speak("hello man")


def listen() :
    r =sr.Recognizer()
    with sr.Microphone() as source :
        lis = 'Listening'
        print(lis,'....')
        
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration=1)
        speak(lis)
        audio = r.listen(source)

    try:
        print('Recognizing...')  
        command = r.recognize_google(audio, language='en-in')
        print('you said {command} \n')
    
    except Exception as e :
        sayagain = 'say that again please'
        print(sayagain,'....')
        #return None
    return command        

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!") 

    
    speak("I am friday version 1.00.01. Please tell me how may I help you")    
    
def search(url):
    webbrowser.open(url)

def chromesearch(url) :
    webbrowser.get('C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s').open(url)

if __name__ == "__main__" :
    speak('hello Sanjay')
    wishMe()
    while True :
    #if 1:
        command = listen().lower()

        if 'wikipedia' in command :
            speak('searching in wikipedia..')
            command = command.replace('wikipedia', '')
            results = wikipedia.summary(command , sentences= 3)
            speak('according to wikipedia..')
            print(results)
            speak(results)
        elif 'open youtube' in command :
            search('youtube.com')
        
        elif 'open google' in command :
            search('www.google.com')
        
        elif 'hello' in command :
            speak('hey how can i help you')

        elif 'play some music' in command :

            if 'spotify' in command :
                os.system('start spotify')
            


        





