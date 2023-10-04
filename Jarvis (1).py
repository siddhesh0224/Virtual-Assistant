import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices)
engine.setProperty('voices',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()



def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >=0 and hour<12:
        speak("Good Morning")

    elif hour >= 12 and hour < 18:
        speak("Good afternoon")

    else:
        speak("Good Evening")

    speak("I am jarvis how may i help you")


def takeCommand():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 0.5
        audio = r.listen(source)

    try :
        print("recognizing")
        query = r.recognize_google(audio,language='en-in')
        print(f"user said : {query}\n")
    
    except Exception as e:
        print(e)
        print("say that again")
        return "None"    
    return query

if __name__ == "__main__":
    wishMe()
    if 1:
        
        query = takeCommand().lower()
        

        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("according to wikipedia")
            print(results)
            speak(results)
        
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open facebook' in query:
            webbrowser.open("facebook.com")
        
        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'smartest' in query:
            speak("Siddhes Pednekar is the smartest man on planet")

        elif 'the time' in query:
            strtime = datetime.datetime.now().strftime("%H:%M:%S")
            print(strtime)
            speak(f"sir the time is {strtime}")
            

        elif 'open code' in query:
            codePath = "C:\\Users\\spedn\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)
        
        elif 'play perfect' in query:
            webbrowser.open("https://www.youtube.com/watch?v=2Vv-BfVoq4g")

     