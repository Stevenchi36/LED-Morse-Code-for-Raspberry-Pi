from gpiozero import LED
import time

converted = {"a":".-","b":"-...","c":"-.-.","d":"-..","e":".","f":"..-.","g":"--.","h":"....","i":"..","j":".---","k":"-.-","l":".-..","m":"--","n":"-.","o":"---","p":".--.","q":"--.-","r":".-.","s":"...","t":"-","u":"..-","v":"...-","w":".--","x":"-..-","y":"-.--","z":"--..","0":"-----","1":".----","2":"..---","3":"...--","4":"....-","5":".....","6":"-....","7":"--...","8":"---..","9":"----."}

led = LED(26)
longTime = 1
shortTime = .5
inputString = ""

def longFlash():
	led.on()
	time.sleep(longTime)
	led.off()
	time.sleep(.2)

def shortFlash():
	led.on()
	time.sleep(shortTime)
	led.off()
	time.sleep(.2)
def space():
	led.on()
	time.sleep(.1)
	led.off()

def getInput():
	return raw_input("Please enter text or type \"quit\" to exit: ")

inputString = getInput().lower()
while (inputString != "quit"):
	for c in inputString:
		if c == " ":
			space()
		elif:
			morseconverted = converted[c]
			for symbol in morseconverted:
				if symbol == "-":
					longFlash()
				elif symbol == ".":
					shortFlash()
				elif symbol == " ":
					space()
	inputString = getInput().lower()