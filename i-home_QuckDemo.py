# i=home: an adaptive smart home

import sys
import os
import speech
import pickle
import serial

on = ['on', 'onn', 'all', 'one', 'an', 'down', 'non', 'known', 'learn', 'grown', 'town', 'fun']
off = ['off', 'of']
light = ['light', 'night', 'knight', 'fight', 'like', 'right', 'write', 'site', 'sight', 'laid']
fan = ['fan', 'fun', 'for', 'fennel', 'friend', 'four', 'fore', 'and', 'fund', 'fend', 'fat']
both = ['both', 'bought', 'boat', 'vote', 'bullet', 'but', 'mood', 'board', 'food', 'bored', 'breath', 'breadth', 'book', 'bullets', 'growth', 'what', 'work']



light_on = "a"
light_off = "b"
fan_on = "c"
fan_off = "d"
both_on = "e"
both_off = "f"
serial_port = 10

def send_serial_data(command):
    ser = serial.Serial(serial_port)
    ser.write(command)
    ser.close()
    
##TrainingDataFile = 'training.data'
##
##
##def add_training_data(spoken_command1, spoken_command2, user_id, TrainingDictionary):
##    fw = open(TrainingDataFile, 'wb')
##    TrainingDictionary[user_id] = [spoken_command1, spoken_command2]
##    pickle.dump(TrainingDictionary, fw)
##    fw.close()
##
##def load_training_data():
##    fr = open(TrainingDataFile, 'rb')
##    TrainingDictionary = pickle.load(fr)
##    fr.close()
##    return TrainingDictionary

    
#def listen_from_user(spoken_command1, spoken_command2, user_id):

#def train_home(spoken_command1, spoken_command2, userid):

#def add_training_set(spoken_command1, spoken_command2, user_id):
    

#add_training_data('both', 'on', 'user2', trd)
    
def activate_home(spoken_command1, spoken_command2):
    if ((spoken_command1 in light) and (spoken_command2 in on)):
        print("The light is switched on")
        send_serial_data(light_on)
        speech.say("The light is switched on")
    elif ((spoken_command1 in light) and (spoken_command2 in off)):
        send_serial_data(light_off)
        print("The light is switched off")
        speech.say("The light is switched off")
    elif ((spoken_command1 in fan) and (spoken_command2 in on)):
        print("The fan is switched on")
        send_serial_data(fan_on)
        speech.say("The fan is switched on")
    elif ((spoken_command1 in fan) and (spoken_command2 in off)):
        print("The fan is switched off")
        send_serial_data(fan_off)
        speech.say("The fan is switched off")
    elif ((spoken_command1 in both) and (spoken_command2 in on)):
        print("Both light and fan are switched on")
        send_serial_data(both_on)
        speech.say("Both light and fan are switched on")
    elif ((spoken_command1 in both) and (spoken_command2 in off)):
        print("Both light and fan are switched off")
        send_serial_data(both_off)
        speech.say("Both light and fan are switched off")
    elif (spoken_command1 == 'exit'):
        speech.say("Goodbye.")
        listener.stoplistening()
        sys.exit()
        
    else:
        print("Sorry, This Command is not recognized by i-home")
        speech.say("Sorry This command is not recognized by i-home")

##def activate_home(spoken_command1, spoken_command2):
##    if ((spoken_command1 in light) and (spoken_command2 in on)):
##        print("light is switched on")
##        speech.say("The lights are switched on")
##    elif ((spoken_command1 in light) and (spoken_command2 in off)):
##        print("light is switched off")
##        speech.say("The lights are switched off")
##    elif ((spoken_command1 in fan) and (spoken_command2 in on)):
##        print("fan is switched on")
##        speech.say("fan is switched on")
##    elif ((spoken_command1 in fan) and (spoken_command2 in off)):
##        print("fan is switched off")
##        speech.say("fan is switched off")
##    elif ((spoken_command1 in both) and (spoken_command2 in on)):
##        print("both light and fan are switched on")
##        speech.say("both light and fan are switched on")
##    elif ((spoken_command1 in both) and (spoken_command2 in off)):
##        print("both light and fan are switched off")
##        speech.say("both light and fan are switched off")
##    elif (spoken_command1 == 'exit'):
##        speech.say("Goodbye.")
##        listener.stoplistening()
##        sys.exit()
##    else:
##        print("This Command is not recognizable by i-home")
##        speech.say("This command is not recognized by i-home")
##    


def callback(phrase, listener):
    #print ": %s" % phrase
    #print(phrase)
    if phrase == "turn off":
        speech.say("Goodbye.")
        listener.stoplistening()
        sys.exit()
    else:
       # print(phrase.split())
        spoken_input = phrase.split()
       # print(spoken_input)
        spoken_command1 = spoken_input[0].lower()
        spoken_command2 = spoken_input[len(spoken_input) - 1].lower()
        #print(spoken_command1)
        #print(spoken_command2)
        activate_home(spoken_command1, spoken_command2)

##print "Anything you type, speech will say back."
##print "Anything you say, speech will print out."
##print "Say or type 'turn off' to quit."
##print

print "i-home is activated"
listener = speech.listenforanything(callback)


while listener.islistening():
    text = raw_input("> ")
    if text == "turn off":
        listener.stoplistening()
        sys.exit()
    else:
        speech.say(text)





