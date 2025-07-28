import speech_recognition as sr
import webbrowser
import pyttsx3
import traceback
import musicLibrary
import requests


# recognizer object
recognizer = sr.Recognizer()

newsapi = "ba89a47c60254bf3bffaf44db161bb81"
# Initialise tts engine


# create a function to convert text to speech
def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def processCommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif "open facebook" in c.lower():
        webbrowser.open("https://facebook.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")
    elif "open linkedin" in c.lower():
        webbrowser.open("https://linkedin.com")
    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1]
        link = musicLibrary.music[song]
        webbrowser.open(link)
    elif "news" in c.lower():

        try:
            r = requests.get(f"https://newsapi.org/v2/top-headlines?country=in&category=technology&apiKey=ba89a47c60254bf3bffaf44db161bb81")
            r.raise_for_status()
            data = r.json()
            articles = data.get('articles', [])
            if not articles:
                speak("No news found.")
            for article in articles[:5]:  # Limit to 5 headlines
                speak(article['title'])
        except Exception as e:
            print("Failed to fetch news:", e)
            speak("Sorry, I couldn't fetch the news.")

        
    



if __name__ == "__main__":
    speak("Initializing Jarvis....")
    while True:
        # Listen for the wake word "Jarvis"
        # obtain audio from the microphone
        r = sr.Recognizer()
         
        print("recognizing...")
        try:
            with sr.Microphone() as source:
                print("Listening...")
                audio = r.listen(source, timeout=2, phrase_time_limit=1)

            word = r.recognize_google(audio)
            
            print("Recognized wake word:", word)  # Add this!

            if "jarvis" in word.lower():
                speak("Ya, how can i help you?")
        
                # Listen for command
                with sr.Microphone() as source:
                    print("Jarvis Active...")
                    audio = r.listen(source, timeout = 5, phrase_time_limit=5)
                    command = r.recognize_google(audio)

                    processCommand(command)


        except Exception as e:
           print("Error; {0}".format(e))