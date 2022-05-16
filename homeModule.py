#Module imports
    #bookingModule
import bookingModule as booking
import varModule as var
import roomInfoModule as room
import roomServiceModule as roomServe
import paymentModule as payment
import recordModule as record
import speech_recognition as sr
from gtts import gTTS
from playsound import playsound
def Home():
	#Intro section
	welcome = "Welcome to Garrison"
	
	output = gTTS(text=welcome, lang=var.lang, slow=False)
	output.save("welcome.mp3")
	print("\t\t\t\t\t\t WELCOME TO HOTEL Garrison\n")
	playsound("welcome.mp3")
	#INtro section end

	#how can we help
	print("\t\t\t 1 Booking\n")
	print("\t\t\t 2 Rooms Info\n")
	print("\t\t\t 3 Room Service(Menu Card)\n")
	print("\t\t\t 4 Payment\n")
	print("\t\t\t 5 Record\n")
	print("\t\t\t 0 Exit\n")
	
	help = "Please tell from above what you want to do"
	output = gTTS(text=help, lang=var.lang, slow=False)
	output.save("help.mp3")
	playsound("help.mp3")
	
	var.hear
	with sr.Microphone() as source:
		print("Listening...")
		audio = var.hear.listen(source)
		try:
			ch = var.hear.recognize_google(audio)
		except:
			print("Please say again")
	# ch=int(input("->"))
	
	if ch == "booking":

		print(" ")
		booking.Booking()
	
	elif ch == 2:
		print(" ")
		room.Rooms_Info()
	
	elif ch == 3:
		print(" ")
		roomServe.restaurant()
	
	elif ch == 4:
		print(" ")
		payment.Payment()
	
	elif ch == 5:
		print(" ")
		record.Record()
	
	else:
		exit()
