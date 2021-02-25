import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser as wb 
import psutil
import smtplib
import pyjokes
import os
import pyautogui
import random
import json
import requests
import time
import wolframalpha
from urllib.request import urlopen
engine = pyttsx3.init()
wolframalpha_app_id = 'your id'
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def time_():
    t = datetime.datetime.now().strftime('%I:%M:%S') #* 24 Hour Clock
    engine.say(t)
    engine.runAndWait()

def date_():
    year = datetime.datetime.now().year
    month = datetime.datetime.now().month
    date = datetime.datetime.now().day
    speak("The Current Date is")
    speak(date)
    speak(month)
    speak(year)

def joke():
    v = pyjokes.get_joke()
    print(v)
    speak(v)

def screenshot_():
    img = pyautogui.screenshot()
    img.save("C:/Users/animi/Desktop/Test/"+str(random.randint(1, 100000))+".png")

def send_email_(to,content):
    try:
        server = smtplib.SMTP('smtp.gmail.com',587)
        server.ehlo()
        server.starttls()
        server.login('testpersonid2@gmail.com','your password')
        server.sendmail('testperson2@gmail.com',to,content)
        server.close()
    except:
        speak("Server Error")

def wishme():
    hour = datetime.datetime.now().hour

    if hour >= 6  and hour <= 12:
        speak('Good Morning Sir')

    elif hour >= 12 and hour < 18:
        speak('Good Afternoon Sir')
    elif hour >= 18 and hour <= 24:
        speak("Good Evening Sir")
    elif hour >= 24 and hour <= 6:
        speak("Good Night Sir")

    speak("Welcome back Animish Sir. I am Cirious.")
    speak("How can I help you Sir!")
def cpu():
    usage = str(psutil.cpu_percent())
    speak("CPU currently is at"+ usage+"%")

def takeCommands():
    r= sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening....')
        r.pause_threshold = 1
        audio = r.listen(source)

        try:
            print("Recognizing...")
            query = r.recognize_google(audio,language='en-IN')
            print(query)

        except Exception as e:
            print(e)
            speak("Couldnot Catch That. Please Say it again sir")
            return "NONE"

        return query

if __name__ == "__main__":
    wishme()
    while True:
        query = takeCommands().lower()

        if 'time' in query:
            time_()
        elif 'date' in query:
            date_()
        elif 'wikipedia' in query:
            speak('Searching about the topic')
            query = query.replace('wikipedia','')
            result = wikipedia.summary(query,sentences=4)
            speak('Accoding To Wikipedia')
            print(result)
            speak(result)
        elif 'send email' in query:
            try:
                speak("What Should I write Sir!")
                content = takeCommands()
                reciever = input("Enter email:-")
                to= reciever
                send_email_(to,content)
                speak(content)
                speak('Email Has Been Sent')

            except Exception as e:
                print(e)
                speak("Unable to send Email")

        elif 'search in firefox' in query:
            speak("What Should I search Sir!")
            chromepath = "C:/Program Files/Firefox Developer Edition/firefox.exe %s"

            search = takeCommands().lower()
            wb.get(chromepath).open_new_tab(search+'.com')

        elif 'search in youtube' in query:
            speak("What Should I search Sir!")
            seach_term = takeCommands().lower()
            speak("Here we go Sir!")
            wb.open("https://www.youtube.com/results?search_query="+seach_term)

        elif 'search in google' in query:
            speak("What to search sir!")
            seach_term = takeCommands().lower()
            speak('here we go')
            wb.open('https://www.google.com/search?q='+seach_term)

        elif 'cpu' in query:
            cpu()
        elif 'joke' in query:
            joke()
        elif 'go offline' in query:
            speak("Going Offline Sir")
            quit()

        elif 'word' in query:
            speak("Opening MS Word")
            ms_word = "C:/Program Files/Microsoft Office/Office15/WINWORD.exe"
            os.startfile(ms_word)

        elif 'write a note' in query:
            speak("What Should I Write sir?")
            notes = takeCommands()
            file = open('notes.txt','w')
            speak("Should I include date and time too sir")
            ans = takeCommands().lower()
            if 'yes' or 'sure' or 'ofcourse': 
                strTime = datetime.datetime.now().strftime('%H:%M:%S')
                file.write(strTime)
                file.write(':-')
                file.write(notes)
                speak("Done Taking Notes Sir!")

        elif 'show notes' in query:
            speak("Showing Notes Sir")
            file = open('notes.txt','r')
            print(file.read())
            speak(file.read())
            
        elif 'screenshot' in query:
            speak("Taking Screenshot Sir!")
            screenshot_()
        elif 'play music' in query:
            songs_dir = "C:/Users/animi/Downloads/Music"
            music = os.listdir(songs_dir)
            speak("What Should I play Sir?!")
            speak("Select a number sir!")
            ans = takeCommands().lower()
            while('number' not in ans and ans!='random' and ans != 'you choose'):
                speak("I could not understand sir. Please try again!")
                ans = takeCommands().lower()
            if 'number' in ans:
                no = int(ans.replace('number',''))
                os.startfile(os.path.join(songs_dir,music[no]))
            elif 'random' or 'you choose' in ans:
                no = random.randint(0,3)
                os.startfile(os.path.join(songs_dir,music[no]))

        elif 'remember that' in query:
            speak("What Should I remember sir!")
            memory = takeCommands()
            remember = open('memory.txt','w')
            print(memory)
            speak("You asked me to remember "+memory)
            remember.write(memory)
            remember.close()

        elif 'remind' in query:
            remember = open('memory.txt','r')
            speak("You asked me to remind you to "+ remember.read() )
        elif 'news' in query:
            try:
                jsonObj = urlopen("http://newsapi.org/v2/top-headlines?country=us&category=entertainment&apiKey=bf8583a946fa40d48b8413ddc00caeca")
                data = json.load(jsonObj)
                i=1

                speak("Here are some news from entertainment section")
                print("Top Headlines Are:-")
                for item in data['articles']:
                    print(str(i)+'.'+item['title'] + '\n')
                    print(item['description'] + '\n')
                    speak(item['title'])
                    speak(item['description'])
                    i += 1

            except Exception as e:
                print(str(e))

        elif 'where is' in query:
            location = query.replace("where is",'')
            if location != 0:
                speak("User asked to locate "+location)
                wb.open_new_tab("https://www.google.com/maps/place/"+location)

        elif 'calculate' in query:
            client = wolframalpha.Client(wolframalpha_app_id)
            indx = query.lower().split().index('calculate')
            query = query.split()[indx +1:]
            res = client.query(''.join(query))
            answer = next(res.results).text
            print("The Answer is : "+answer)
            speak("The Answer is "+answer)

        elif 'what is' in query or 'who is' in query:
            client = wolframalpha.Client(wolframalpha_app_id)
            res = client.query(query)
            try:
                print(next(res.results).text)
                speak(next(res.results).text)
            except StopIteration:
                print("No Results")

        elif 'stop listening' in query:
            speak("For How many second should I not listen to your command, Sir?")
            ans = int(takeCommands())
            if ans != None:
                time.sleep(ans)
                print(ans)
                speak("I am back at your service Sir.")
            else:
                ans = int(takeCommands())
        elif 'log out' in query:
            os.system("shutdown -l")
        elif "restart" in query:
            os.system("shutdown /r /t 1")
        elif "shutdown" in query:
            os.system("shutdown /s /t 1")
