import speech_recognition as sr
import webbrowser
import pyttsx3
import subprocess
import requests
import json
from win10toast_persist import ToastNotifier
from datetime import date

engine = pyttsx3.init()
engine.setProperty('volume', 1.0 )
engine.setProperty('rate', 190)

def rozpoznaj(msg="Powiedz coś!"):
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print(msg)
        audio = r.listen(source)
        try:
            recognised_text = r.recognize_google(audio, language="pl-PL");
            print("Powiedziałeś "+ recognised_text)
            return recognised_text.lower()
        except sr.UnknownValueError:
            print("Nie mogłem zrozumieć co powiedziałeś!")
        except sr.RequestError as e:
            print("Coś poszło nie tak, a dokładniej ", e)

text = rozpoznaj()
word_list = text.split(" ")
if("otwórz" in text and word_list[0] == "otwórz") or ("uruchom" in text and word_list[0] == "uruchom"):
    if "przeglądarkę" in text:
        engine.say("Otwieram przeglądarke")
        engine.runAndWait()
        webbrowser.open_new_tab("https://www.google.com/")

elif text =="Jaka jest pogoda":
    subprocess.call("explorer.exe shell:appsFolder\\Microsoft.BingWeather_8wekyb3d8bbwe!App", shell=True, 
                    stdout=subprocess.PIPE)