import pyttsx3
import speech_recognition

speaker = pyttsx3.init()
speaker.say("welcome Sir, hi no0r")
speaker.runAndWait()

import speech_recognition as sr

# with sr.Microphone() as source:
#     print("PLease Speak Something✌")
#     voice = Microphone.listen(source)
#     text = Microphone.recognize_google(voice)
#     print("you said this: ",text)