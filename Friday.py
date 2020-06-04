import pyttsx3
import datetime
import time
import speech_recognition as sr
import webbrowser
import wikipedia
from gtts import gTTS
import os
from PyDictionary import PyDictionary
import smtplib


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[2].id)
engine.setProperty('voice',voices[1].id)

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
        print('you said ',command,'\n')
    
    except Exception as e :
        sayagain = 'say that again please'
        print(sayagain,'....')
        return audio
    return command        

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!") 

    
    speak("I am friday version 1.00.02. Please tell me how may I help you")    
    
def search(url):
    webbrowser.open(url)

def chromesearch(url) :
    webbrowser.get('C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s').open(url)

def sendemail(to,content) :
    server = smtplib.SMTP('smpt.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('gmail','password')
    server.sendmail('email',to,content)
    server.close

if __name__ == "__main__" :
    speak('hello Sanjay')
    wishMe()
    while True :
    #if 1:
        command = listen().lower()

        if 'wikipedia' in command :
            speak('searching in wikipedia..')
            command = command.replace('wikipedia', '')
            results = wikipedia.summary(command , sentences= 2)
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

           # if 'spotify' in command :
                os.system('start spotify')
        
        elif 'time' in command:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak("Sir, the time is ")
            speak(strTime)

        #elif 'find the meaning' in command :
        #    end = command.find(' ')        
         #   data = command[0 : end]
          #  meaning = PyDictionary().meaning(data)
           # speak(meaning)

        #elif 'what' in command :
          #  webbrowser.open_new_tab(command)
            
        elif 'send mail' in command :
            try:
                speak('what is the subject')
                subject = listen()
                speak('what should i say')
                message = listen()
                content = 'subject: {}\n\n{}'.format(subject,message)
                speak('whom to send')
                to = listen()
                sendemail(to,content)
                speak('email has been sent!')
            except Exception as e:
                print(e)
                speak('Sorry. I am unable to send this mail.')
        





