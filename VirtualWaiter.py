import pyttsx3
import speech_recognition
en=pyttsx3.init()
class item:
	def __init__(self,name,price):
		self.name=name
		self.price=price
def narrate(sound):
	en.say(sound)
	en.runAndWait()
r=speech_recognition.Recognizer()
def listen_voice():
	global text
	with speech_recognition.Microphone() as source:
		print("Listening")
		audio=r.listen(source)
		text=r.recognize_google(audio)
		print("You said:{}".format(text))
		narrate("You said:{}".format(text))
		


f=item("fruit",'50')
t=item("milk",'11')
available_item_list=[f,t]
bill=0
def processOrder():
	ordered_item=[]
	bill=0
	for each_item in available_item_list:
		if each_item.name in text:
			print(each_item.name) 
			ordered_item.append(each_item.name)
	for dish in ordered_item:
		for each_item in available_item_list:
			if dish==each_item.name:
				bill=bill+int(each_item.price)
	
	return bill

listen_voice()
if 'waiter' in text:
	greeting="Welcome...Please place the order"
	narrate(greeting)
	listen_voice()
	bill=processOrder()
	if bill==0:
		narrate("These items are out of stock")
	else:
		narrate("your bill is: "+str(bill))
	narrate("Please visit again")

	

