# from pip import main
import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib
import requests
from bs4 import BeautifulSoup


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  

    speak("sir")

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 0.5
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)    
        print("Sorry, I could not understand. Could you please say that again?") 
        speak("Sorry, I could not understand. Could you please say that again?") 
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('mahendravpatil3@gmail.com', '0122345')
    server.sendmail('mukulakhairnar05@gmail.com', to, content)
    server.close()

if __name__ == "__main__":
    wishMe()
    while True:
    # if 1:
        query = takeCommand().lower()

        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif "temperature" in query:
            search = "temperature in shirpur-warwade"
            url = f"https://www.google.com/search?q={search}"
            r = requests.get(url)
            data = BeautifulSoup(r.text,"html.parser")
            temp = data.find("div",class_="BNeawe").text
            speak(f"current {search} in {temp}")
            print(f"current {search} in {temp}")

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")

        elif 'open spotify' in query:
            webbrowser.open("spotify.com")

        elif 'play music' in query:
            music_dir = 'D:\\Disco'
            songs = os.listdir(music_dir)
            print(songs)    
            os.startfile(os.path.join(music_dir, songs[1]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")
            print(f"{strTime}")

        elif 'open calculator' in query:
            codePath = "C:\\Windows\\System32\\calc.exe"
            os.startfile(codePath)


        elif 'open code' in query:
            codePath = "C:\\Users\\lenovo\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif 'email to mukul' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "mukulakhairnar05@gmail.com"    
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry sir. I am not able to send this email")

        elif 'what can you do' in query:
            li_commands = {
            "open websites": "Example: 'open youtube.com    ",
            "time": "Example: 'what time it is?'    ",
            "date": "Example: 'what date it is?'    ",
            "launch applications": "Example: 'launch google'    ",
            "weather": "Example: 'what weather/temperature in current location'  ",
            "hello": "Example: interaction with rohini  ",
            "open my computer": "it's open the computer ",
            "open cmd": "it's open command prompt ",
            "open calculator": "it's open calculator ",
            "play music" : "it's play music",
            }
            ans = """I can do lots of things, for example you can ask me time, date, weather in your city,
            I can open websites for you, launch application and more. See the list of commands-"""
            print(ans) 
            print(li_commands)  
            speak(ans)

        elif 'hello' in query:
            print("hello! sir, my name is Rohini.")
            print("how can i help you?")
            speak("hello! sir, my name is Rohini.")
            speak("how can i help you?")
        
        elif 'open my computer' in query:
            codePath = "C:\Windows\explorer.exe"
            os.startfile(codePath)

        elif 'open cmd' in query:
            os.system('start cmd')
        

        

    