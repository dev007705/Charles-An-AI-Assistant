import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
from newsapi import NewsApiClient

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)

def speak(audio):
       engine.say(audio)
       engine.runAndWait()

def wishMe():
      hour=int(datetime.datetime.now().hour)
      if hour>=0 and hour<12:
          speak("good morning sir")
      elif hour>=12 and hour<18:
          speak("good afternoon sir")
      else:
          speak("good evening sir")

      speak("Please tell me how may I help you?")

def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
          print("Listening...")
          r.pause_threshold = 1
          r.energy_threshold = 400
          audio=r.listen(source)
    try:
        print("Recognizing...")
        query=r.recognize_google(audio,language='en-in')
        print(f"User said:{query}\n")

    except Exception as e:
        print("say that again please")
        return "None"
    return query

if __name__ == "__main__":
    
    wishMe()
    while True:
        query=takeCommand().lower()
        if 'wikipedia' in query:
            speak('searching wikipedia...')
            query=query.replace("wikipedia","")
            results=wikipedia.summary(query,sentences=2)
            speak("According to wikipedia")
            speak(results)
        elif 'youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open('google.com')

        elif 'play music' in query:
            music_dir = 'C:\\Users\\hp\\Music\\Music files'
            songs=os.listdir(music_dir)
            os.startfile(os.path.join(music_dir,songs[0]))
        
        elif 'the time' in query:
            strTime=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")

        elif 'kitna baja hai' in query:
            strTime=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")

        elif 'who are you' in query:
            speak("I am Charles, an AI assistant developed by Devendra Kumar")

        elif 'search' in query:
            speak('searching...')
            results=webbrowser.open(query)
            speak("According to google")

        elif 'play video' in query:
            video_dir = 'C:\\Users\\hp\\Videos'
            videos=os.listdir(video_dir)
            os.startfile(os.path.join(video_dir,videos[7]))
            
        elif 'who is' in query:
            speak('searching...')
            results=webbrowser.open(query)
            speak("According to google")

        elif 'what is' in query:
            speak('searching...')
            results=webbrowser.open(query)
            speak("According to google")

        elif 'pagal ho kya' in query:
            speak('I am not mad. I am the smartest assistant')

        elif 'news' in query:
           newsapi = NewsApiClient(api_key='ac3d2585f2ee4eeab2e8d88272cb8fb6')
           all_articles = newsapi.get_everything(q='bitcoin',
                                      sources='abc-news',
                                      domains='abcnews.go.com',
                                      from_param='2019-06-16',
                                      to='2017-06-16',
                                      language='en',
                                      sort_by='popularity',
                                      page=1)
           speak(all_articles)

        
        
        




