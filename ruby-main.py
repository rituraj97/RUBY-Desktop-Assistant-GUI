from tkinter import *
import numpy as np
import cv2
import PIL.Image, PIL.ImageTk
import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import random
import smtplib
import pyowm
from PIL import Image
import requests



def get_location():
    """ Function To Print GeoIP Latitude & Longitude """
    ip_request = requests.get('https://get.geojs.io/v1/ip.json')
    my_ip = ip_request.json()['ip']
    geo_request = requests.get('https://get.geojs.io/v1/ip/geo/' +my_ip + '.json')
    geo_data = geo_request.json()
    geo = geo_data['city']
    return geo

a = {'name':'example123@gmail.com'}                 #replace with valid name and email id
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

window = Tk()

global var
global var1

var = StringVar()
var1 = StringVar()

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def sendemail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('example-master@gmail.com', 'app-password')            #replace with master/sender email id and app-password generated from email provider
    server.sendmail('example-master@gmail.com', to, content)
    server.close()

def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour <= 12:
        var.set("Good Morning Sir") 
        window.update()
        speak("Good Morning Sir!")
    elif hour >= 12 and hour <= 18:
        var.set("Good Afternoon Sir!")
        window.update()
        speak("Good Afternoon Sir!")
    else:
        var.set("Good Evening Sir")
        window.update()
        speak("Good Evening Sir!")
    speak("Myself Ruby! How may I help you sir") 

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        var.set("Listening...")
        window.update()
        print("Listening...")
        r.pause_threshold = 1
        r.energy_threshold = 400
        audio = r.listen(source)
    try:
        var.set("Recognizing...")
        window.update()
        print("Recognizing")
        query = r.recognize_google(audio, language='en-in')
    except Exception as e:
        return "None"
    var1.set(query)
    window.update()
    return query

def play():
    btn2['state'] = 'disabled'
    btn0['state'] = 'disabled'
    btn1.configure(bg = 'orange')
    wishme()
    while True:
        btn1.configure(bg = 'orange')
        city=get_location()
        if city=="Puducherry":
            var.set("You are in Puducherry")
            window.update()
        else:
            var.set(f"You are in {city}")
            window.update()
            speak(f"You are in {city}. Go to Puducherry first.")
            continue
        query = takeCommand().lower()
        if 'exit' in query:
            var.set("Bye sir")
            btn1.configure(bg = '#5C85FB')
            btn2['state'] = 'normal'
            btn0['state'] = 'normal'
            window.update()
            speak("Bye sir")
            break

        elif 'wikipedia' in query:
            if 'open wikipedia' in query:
                webbrowser.open('wikipedia.com')
            else:
                try:
                    speak("searching wikipedia")
                    query = query.replace("according to wikipedia", "")
                    results = wikipedia.summary(query, sentences=2)
                    speak("According to wikipedia")
                    var.set(query)
                    window.update()
                    speak(results)
                except Exception as e:
                    var.set('sorry sir could not find any results')
                    window.update()
                    speak('sorry sir could not find any results')

        elif 'open youtube' in query:
            var.set('opening Youtube')
            window.update()
            speak('opening Youtube')
            webbrowser.open("youtube.com")

        elif 'open course error' in query:
            var.set('opening coursera')
            window.update()
            speak('opening coursera')
            webbrowser.open("coursera.com")

        elif 'open google' in query:
            var.set('opening google')
            window.update()
            speak('opening google')
            webbrowser.open("google.com")

        elif 'say hello' in query:
            var.set('Hello Everyone! My self Ruby')
            window.update()
            speak('Hello Everyone! My self Ruby')

        elif 'hello' in query:
            var.set('Hello Sir')
            window.update()
            speak("Hello Sir")
			
        elif 'open stackoverflow' in query:
            var.set('opening stackoverflow')
            window.update()
            speak('opening stackoverflow')
            webbrowser.open('stackoverflow.com')

        elif ('play music' in query) or ('change music' in query):
            var.set('Here are your favorites')
            window.update()
            speak('Here are your favorites')
            music_dir = 'path-to\\songs'                                #enter valid path to songs folder
            songs = os.listdir(music_dir)
            n = random.randint(0,3)
            os.startfile(os.path.join(music_dir, songs[n]))

        elif 'the time' in query:
            strtime = datetime.datetime.now().strftime("%H:%M:%S")
            var.set("Sir the time is %s" % strtime)
            window.update()
            speak("Sir the time is %s" %strtime)

        elif 'the date' in query:
            strdate = datetime.datetime.today().strftime("%d %m %y")
            var.set("Sir today's date is %s" %strdate)
            window.update()
            speak("Sir today's date is %s" %strdate) 

        elif 'thank you' in query:
            var.set("Welcome Sir")
            window.update()
            speak("Welcome Sir")

        elif 'can you do for me' in query:
            var.set('I can do multiple tasks for you sir.\n tell me whatever you want to perform sir')
            window.update()
            speak('I can do multiple tasks for you sir. tell me whatever you want to perform sir')

        elif 'old are you' in query:
            var.set("I am a little baby sir")
            window.update()
            speak("I am a little baby sir")

        elif 'open media player' in query:
            var.set("opening VLC media Player")  
            window.update()
            speak("opening V L C media player")
            path = "path-to\\vlc.exe"                                       #Enter valid path for vlc.exe
            os.startfile(path)

        elif 'your name' in query:
            var.set("Myself Ruby Sir")
            window.update()
            speak('myself Ruby sir')

        elif 'who created you' in query:
            var.set('My Creators are Ankit and Rituraj.')
            window.update()
            speak('My Creators are Ankit and Rituraj')

        elif 'weather' in query:
            owm = pyowm.OWM('api-key')                 #open weather map API key
            #current weather forecast
            loc = owm.weather_at_place(city)
            weather = loc.get_weather()
            #status
            status = weather.get_detailed_status()
            var.set(f'{status} in {city}')
            window.update()
            speak(f'{status} in {city}')
            # temperature
            temp = weather.get_temperature(unit='celsius')
            for key,val in temp.items():
                    if key == 'temp':
                            var.set(f'{val} degree celcius')
                            window.update()
                            speak(f"current temperature is {val} degree celcius")
            # humidity, wind, rain, snow
            humidity = weather.get_humidity()
            wind = weather.get_wind()
            var.set(f'{humidity} grams per cubic meter')
            window.update()
            speak(f'humidity is {humidity} grams per cubic meter')
            var.set(f'wind {wind}')
            window.update()
            speak(f'wind {wind}')
            # sun rise and sun set
            sr = weather.get_sunrise_time(timeformat='iso')
            ss = weather.get_sunset_time(timeformat='iso')
            var.set(sr)
            window.update()
            speak(f'SunRise time is {sr}')
            var.set(ss)
            window.update()
            speak(f'SunSet time is {ss}')
            # clouds and rain
            loc = owm.three_hours_forecast(city)
            clouds = str(loc.will_have_clouds())
            rain = str(loc.will_have_rain())
            if clouds == 'True':
                    var.set("It may have clouds in next 5 days")
                    window.update()
                    speak("It may have clouds in next 5 days")
            else:
                    var.set("It may not have clouds in next 5 days")
                    window.update()
                    speak("It may not have clouds in next 5 days")
            if rain == 'True':
                    var.set("It may rain in next 5 days")
                    window.update()
                    speak("It may rain in next 5 days")
            else:
                    var.set("It may not rain in next 5 days")
                    window.update()
                    speak("It may not rain in next 5 days")


        elif 'email to' in query:
            try:
                query = query.replace("email to", "")
                query = query.replace(" ", "")
                print(query)
                var.set("What should I say")
                window.update()
                speak('what should I say')
                content = takeCommand()
                to = a[query]
                sendemail(to, content)
                var.set('Email has been sent!')
                window.update()
                speak('Email has been sent!')

            except Exception as e:
                print(e)
                var.set("Sorry Sir! I was not able to send this email")
                window.update()
                speak('Sorry Sir! I was not able to send this email')
		
        elif 'open code blocks' in query:
            var.set('Opening Codeblocks')
            window.update()
            speak('opening Codeblocks')
            os.startfile("path-to\\codeblocks.exe") 

        elif 'open anaconda' in query:
            var.set('Opening Anaconda')
            window.update()
            speak('opening anaconda')
            os.startfile("path-to\\Anaconda Navigator (Anaconda3)")

        elif 'click photo' in query:
            stream = cv2.VideoCapture(0)
            grabbed, frame = stream.read()
            if grabbed:
                cv2.imshow('pic', frame)
                cv2.imwrite('pic.jpg',frame)
            stream.release()

        elif 'record video' in query:
            cap = cv2.VideoCapture(0)
            out = cv2.VideoWriter('output.avi', cv2.VideoWriter_fourcc(*"MJPG"), 30,(640,480))
            while(cap.isOpened()):
                ret, frame = cap.read()
                if ret:
                    
                    out.write(frame)

                    cv2.imshow('frame',frame)
                    if cv2.waitKey(1) & 0xFF == ord('q'):
                        break
                else:
                    break
            cap.release()
            out.release()
            cv2.destroyAllWindows()
              
def update(ind):
    frame = frames[(ind)%100]
    ind += 1
    label.configure(image=frame)
    window.after(100, update, ind)

label2 = Label(window, textvariable = var1, bg = '#FAB60C')
label2.config(font=("Courier", 20))
var1.set('User Said:')
label2.pack()

label1 = Label(window, textvariable = var, bg = '#ADD8E6')
label1.config(font=("Courier", 20))
var.set('Welcome')
label1.pack()

frames = [PhotoImage(file='assist.gif',format = 'gif -index %i' %(i)) for i in range(100)]
window.title('RUBY')

label = Label(window, width = 500, height = 500)
label.pack()
window.after(0, update, 0)

btn0 = Button(text = 'WISH ME',width = 20, command = wishme, bg = '#5C85FB')
btn0.config(font=("Courier", 12))
btn0.pack()
btn1 = Button(text = 'START',width = 20,command = play, bg = '#5C85FB')
btn1.config(font=("Courier", 12))
btn1.pack()
btn2 = Button(text = 'EXIT',width = 20, command = window.destroy, bg = '#5C85FB')
btn2.config(font=("Courier", 12))
btn2.pack()


window.mainloop()
