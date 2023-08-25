import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import pyaudio
import pywhatkit


engine = pyttsx3.init('sapi5')
engine.setProperty('rate', 190)
engine.setProperty('volume', 1.0)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


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
    speak("I am DAVID. I am your personal AI voice assistant. How may I help you?")



def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        print(e)
        print("Sorry, I could not understand. Could you please say that again...")
        speak("Sorry, I could not understand. Could you please say that again...")
        takeCommand()
        return "None"
    return query
    


if __name__ == "__main__":
    wishMe()

    
    if 1:
        query = takeCommand().lower()
      
    
        
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query, sentences=2)
            print(results)
            speak(results)

        
        
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")



        elif 'open google' in query:
            webbrowser.open("google.com")



        elif 'open v top' in query:
            webbrowser.open("https://vtop.vitbhopal.ac.in/vtop/initialProcess")

        
        elif 'open v-top' in query:
            webbrowser.open("https://vtop.vitbhopal.ac.in/vtop/initialProcess")


        elif 'open wetop' in query:
            webbrowser.open("https://vtop.vitbhopal.ac.in/vtop/initialProcess")


        elif 'open vetop' in query:
            webbrowser.open("https://vtop.vitbhopal.ac.in/vtop/initialProcess")


        elif 'open ms teams' in query:
            codePath= "C:\\Users\\neil1\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Microsoft Teams (work or school).lnk"
            os.startfile(codePath)



        elif 'open vlc' in query:
            codePath= "C:\\Program Files\\VideoLAN\\VLC\\vlc.exe"
            os.startfile(codePath)



        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The time is {strTime}")


        elif 'to code' in query:
            codePath = "C:\\Users\\neil1\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)


        
        elif 'do coding' in query:
            codePath =  "C:\\Users\\neil1\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)



        elif 'open chat gpt' in query:
             webbrowser.open("https://chat.openai.com/chat")



        elif 'best teacher' in query:
            speak("Hari haran sir is the best Teacher.")

        

        elif 'open word' in query:
            codePath= "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Word.lnk"
            os.startfile(codePath)



        elif 'make a presentation' in query:
            codePath= "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\PowerPoint.lnk"
            os.startfile(codePath)



        elif 'open brave' in query:
            codePath= "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Brave.lnk"
            os.startfile(codePath)



        elif 'open excel' in query:
            codePath= "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Excel.lnk"
            os.startfile(codePath)



        elif 'listen to music' in query:
            webbrowser.open("https://open.spotify.com/")



        elif 'play games' in query:
            codePath= "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Epic Games Launcher.lnk"
            os.startfile(codePath)



        elif 'send an email' in query:
            webbrowser.open("https://mail.google.com/mail/u/2/#inbox")



        elif 'online shopping' in query:
            webbrowser.open("https://www.amazon.in/?ie=UTF8&tag=googmantxtmob50-21&ascsubtag=_k_Cj0KCQjwy5maBhDdARIsAMxrkw3ofV2leuya4G_WZXDmpYli4RVI7NCtQHpOY6aTItZXmQU3_h-XqAQaAvcREALw_wcB_k_&gclid=Cj0KCQjwy5maBhDdARIsAMxrkw3ofV2leuya4G_WZXDmpYli4RVI7NCtQHpOY6aTItZXmQU3_h-XqAQaAvcREALw_wcB")

    

        elif 'how are you' in query:
            speak("I am fine. What about you?")

    