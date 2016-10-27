from gpiozero import LED
import time

#Python dictionary containing characters and the matching morse code
converted = {"a":".-","b":"-...","c":"-.-.","d":"-..","e":".","f":"..-.","g":"--.","h":"....","i":"..","j":".---","k":"-.-","l":".-..","m":"--","n":"-.","o":"---","p":".--.","q":"--.-","r":".-.","s":"...","t":"-","u":"..-","v":"...-","w":".--","x":"-..-","y":"-.--","z":"--..","0":"-----","1":".----","2":"..---","3":"...--","4":"....-","5":".....","6":"-....","7":"--...","8":"---..","9":"----.",".":".-.-.-",",":"--..--",":":"---...","?":"..--..","'":".----.","-":"-....-","/":"-..-.","(":"-.--.-",")":"-.--.-","\"":".-..-.","@":".--.-.","=":"-...-"}

led = LED(26)                   #Assign pin #26 to a variable
speed = 1                       #Change to proportionately alter speed
longTime = .3 * speed           #Duration of the dash
shortTime = .1 * speed          #Duration of the period
spaceTime = .7 * speed          #Duration between words
betweenCharTime = .3 * speed    #Duration between characters
inputString = ""

#Flash LED for the dash
def longFlash():
	led.on()
	time.sleep(longTime)
	led.off()

#Flash LED for the period
def shortFlash():
	led.on()
	time.sleep(shortTime)
	led.off()

#Sleep for time of a space
def space():
	time.sleep(spaceTime)

#Ask for input
#returns the input
def getInput():
	return raw_input("Please enter text or type \"quit\" to exit: ")

#Make input lowercase and assign it to a variable
inputString = getInput().lower()
#While the input isn't "quit"
while (inputString != "quit"):
	#Go through each character of the input
	for c in inputString:
		#If it is a space
		if c == " ":
			space()
		#If it is in the dictionary
		elif c in converted:
			#convert character to the morse code
			morseconverted = converted[c]
			#goes through each character in the morse code
			for symbol in morseconverted:
				#If the symbol is a dash
				if symbol == "-":
					longFlash()
					time.sleep(betweenCharTime)
				#If the symbol is a period
				elif symbol == ".":
					shortFlash()
					time.sleep(betweenCharTime)
				#If the symbol is somehow not a dash or period
				else:
					print "Not a '-' or '.'"
		#If the character is not supported in the dictionary
		else:
			print "'" + c + "'" + " is not a supported character"
	#Ask for input again
	inputString = getInput().lower()