from gtts import gTTS
import os
from playsound import playsound
import speech_recognition as sr
import varModule as var


with sr.Microphone() as source:
    print("Listening...")
    audio = var.hear.listen(source)
    try:
        text = var.hear.recognize_google(audio)
        # text = "Hello world"
        language = "en"
        output = gTTS(text="Your sentence was "+text, lang=language, slow=False)
        output.save("result.mp3")
        playsound("result.mp3")
        print(text)
    except:
        print("Please speak again")


# os.system("start result.mp3")