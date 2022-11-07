import psutil
import pyttsx3 as py
import speech_recognition as sr
import datetime
engine=py.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
def speak(*audio):
    for i in range(len(audio)):
        engine.say(audio[i])
        engine.runAndWait()
def wish():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good morning")
    elif hour>=12 and hour<18:
        speak("Good afternoon")
    else:
        speak("Good night")
def how():
    speak("i am good. Hope you are having a great day")
def takecommand():
    s=sr.Recognizer()
    with sr.Microphone() as source:
        s.pause_threshold=0.5
        audio= s.listen(source,None,10)
        try:
            query=s.recognize_google(audio,language='en-in')
        except:
            takecommand()
        query=query.lower()
        if "maansi" in query:
            with sr.Microphone() as source:
                print("listening")
                speak("listening")
                s.pause_threshold=0.5
                audio= s.listen(source)
            try:
                print("recognising.....")
                query=s.recognize_google(audio,language='en-in')
                print("user said:",{query})
                if "battery" in query and "tell" in query:
                    battery()
                elif "wish" in query:
                    wish()
                elif "time" in query:
                    telltime()
                elif "thank you" in query:
                    speak("it's my pleasure")
                    print("it's my pleasure")
                elif "how are you" in query:
                    how()
                    print("i am good. Hope you are having a great day")
                
            except:
                print("please say again")
                takecommand()
        takecommand()
def telltime():
    t=datetime.datetime.now().strftime("%H:%M:%S")
    print(t)
    speak(t)
def convertTime(seconds):
    min=seconds//60
    hour=min//60
    min=min%60
    seconds=seconds%60
    print(hour,":",min,":",seconds)
def battery():
    battery = psutil.sensors_battery()
    
    print("Battery percentage : ", battery.percent)
    speak(f"your battery percentage is {battery.percent}")
    print("Power plugged in : ", battery.power_plugged)
    
    print("battery will ran out in ",end="")
    convertTime(battery.secsleft)



speak("listening")

print("listening")
takecommand()
    

    
    

