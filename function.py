import bookingModule as booking
import varModule as var
import roomInfoModule as room
import roomServiceModule as roomServe
import paymentModule as payment
import recordModule as record
import speech_recognition as sr
from gtts import gTTS
from playsound import playsound

def record():
    var.hear
    with sr.Microphone() as source:
        var.hear.adjust_for_ambient_noise(source)
        print("Listening...")
        audio = var.hear.listen(source)
        try:
            text = var.hear.recognize_google(audio)
            return text
        except:
            print("Could not listene")
     

def tts(text,fileName):
    var.hear
    wname = gTTS(text=text, lang=var.lang, slow=False)
    wname.save(fileName+".mp3")
    playsound(fileName+".mp3")