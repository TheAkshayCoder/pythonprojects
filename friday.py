import pyttsx3
import wikipedia
import webbrowser
import os
import random
import smtplib

myName='friday'

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

#speak('helloo!, I am Gideon, ann interactive Artificial voice Assistant. How can I help you?')
import datetime
def wishme():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good morning!")
    elif hour>=12 and hour<18:
        speak('Good Afternoon!')
    else:
        speak("Good evening!")

    speak("I am Gideon, ann Interactive Artificial Voice Assistant. How can I help you?")

#wishme()

import speech_recognition as sr

def takeCommand():
    ''' This function is used to take the microphone input from the user and returns the output'''
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold=1
        audio=r.listen(source)

    try:
        print('Recoginising...')
        quary=r.recognize_google(audio, language='en-in')
        print(f'User said: {quary}\n')
    except Exception as e:
        print(e)    

        print('Say that again please......')

        return 'None'
    return quary

def sendEmail(to, content):
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('your_email.com','your_account password')
    server.sendmail('your_email.com',to,content)
    server.close()

if __name__ == "__main__":
    wishme()
    while True:
        quary=takeCommand().lower()

        #Logic for executing task based on query
        if 'wikipedia' in quary:
            speak('Searching for your answer in wikipedia... Please wait...')
            quary=quary.replace('wikipedia','')
            results=wikipedia.summary(quary,sentences=2)
            speak('According to wikipedia')
            print(results)
            speak(results)

        if "that's good to know" in quary:
            speak('Thank you so much, Its an owner working with you')

        
        
        elif 'open youtube' in quary:
            webbrowser.open('youtube.com')

        elif 'open google' in quary:
            webbrowser.open('google.com')

        elif 'open stackoverflow' in quary:
            webbrowser.open('stackoverflow.com')

        elif 'play music' in quary:
            music_dir='C:\\Users\\Akshay Thakur\\Desktop\\New folder\\songs'
            songs=os.listdir(music_dir)
           # print(songs)
           # n=random.randint(0,6)
            os.startfile(os.path.join(music_dir,songs[0]))

        elif 'the time' in quary:
            strTime=datetime.datetime.now().strftime('%H:%M:%S')
            speak(f'Sir the time is {strTime}')

        elif 'open code' in quary:
            codepath='"C:\\Users\\Akshay Thakur\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"'
            os.startfile(codepath)

        elif 'email to akshay' in quary:
            try:
                speak('What should I say?')
                content=takeCommand()
                to='your_email.com'
                sendEmail(to, content)
                speak('Email has been sent!')
            except Exception as e:
                print(e)
                speak('Sorry email is not sent')

        elif 'google search' in quary:
            speak('What do you want to search in google?')
            query2=takeCommand().lower()
            try: 
                from googlesearch import search
            except ImportError:  
                print("No module named 'google' found")
  
            for j in search(query2, tld="co.in", num=10, stop=10, pause=2): 
                print(j)   

        elif 'open chrome' in quary:
            try:
                speak('Trying to open chrome... Please wait....!')
            
                c=webbrowser.get('chrome')
                c.open('https://www.youtube.com//watch?v=nhNR2TZREO4&ab_channel=Tech-GramAcademy')
            except Exception as e:
                print(e)
                speak('Sorry chrome can''nt be opened')            

        elif 'nice job' in quary:
            speak('Thank you so much!')    

        elif 'exit' in quary:
            speak("It's a pleasure working with you!")
            break
        
        else:
            speak('I did not get you. Please speak that again')
        



        





