# Say anything you type, and write anything you say.
# Stops when you say "turn off" or type "turn off".

import speech
import sys
import os

def activate_home(spoken_command):
    if ((spoken_command == 'on') or (spoken_command == 'onn')):
       # print("I am calling ON.EXE")
        os.system("on.exe")
        #os.system("killon.bat")
        #print("SUCCESSFUL")
        #speech.say("The lights are switched on")
    elif ((spoken_command == 'of') or (spoken_command == 'off')):
        #print("I am calling OFF.EXE")
        os.system("off.exe")
        #os.system("killon.bat")
        #print("SUCCESS")
        #speech.say("The lights are switched off")
    elif (spoken_command == 'exit'):
#        speech.say("Goodbye.")
        listener.stoplistening()
        sys.exit()
    else:
        print("This Command is not recognizable by i-home")
        #speech.say("This command is not recognized by i-home")


    
def callback(phrase, listener):
    print ": %s" % phrase
    if phrase == "turn off":
        speech.say("Goodbye.")
        listener.stoplistening()
        sys.exit()
    else:
       # print(phrase.split())
        spoken_input = phrase.split()
       # print(spoken_input)
        spoken_command = spoken_input[len(spoken_input) - 1]
       # print(spoken_command)
        activate_home(spoken_command)

#print "Anything you type, speech will say back."
#print "Anything you say, speech will print out."
#print "Say or type 'turn off' to quit."
print

listener = speech.listenforanything(callback)

while listener.islistening():
    text = raw_input("> ")
    if text == "turn off":
        listener.stoplistening()
        sys.exit()
    else:
        speech.say(text)
