from gpiozero import LED
import time

converted = ["a":".-","b":"-...","c":"-.-.","d":"-..","e":".","f":"..-.","g":"--.","h":"....","i":"..","j":".---","k":"-.-","l":".-..","m":"--","n":"-.","o":"---","p":".--.","q":"--.-","r":".-.","s":"...","t":"-","u":"..-","v":"...-","w":".--","x":"-..-","y":"-.--","z":"--..",0:"-----",1:".----",2:"..---",3:"...--",4:"....-",5:".....",6:"-....",7:"--...",8:"---..",9:"----."]

led = LED(26)
longTime = 1
shortTime = .5

def longFlash():
	led.on()
	time.sleep(longTime)
	led.off()

def shortFlash():
	led.on()
	time.sleep(shortTime)
	led.off()

def getInput():
	inputString = raw_input("Please enter text or type quit to exit: ")

getInput()
