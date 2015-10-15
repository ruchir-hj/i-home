# i=home: an adaptive smart home

import sys
import os
import speech
import pickle
import pyfaces
import serial

on = ['on', 'onn', 'all', 'one', 'an', 'down', 'non', 'known', 'learn', 'grown', 'town', 'fun']
off = ['off', 'of']
light = ['light', 'night', 'knight', 'fight', 'like', 'right', 'write', 'site', 'sight', 'laid']
fan = ['fan', 'fun', 'for', 'fennel', 'friend', 'four', 'fore', 'and', 'fund', 'fend', 'fat']
both = ['both', 'bought', 'boat', 'vote', 'bullet', 'but', 'mood', 'board', 'food', 'bored', 'breath', 'breadth', 'book', 'bullets', 'growth', 'what', 'work']
personal = ['yes', 'yeah', 'yes yes', 'and yes', 'yep', 'yup', 'this']
default = ['no', 'new', 'know', 'knew', 'view', 'none', 'nope']

TrainingDataFile = 'training.data'
Mode = 'default'
done=0
turn_off=0
user_id = ''

light_on = "a"
light_off = "b"
fan_on = "c"
fan_off = "d"
both_on = "e"
both_off = "f"
serial_port = 10

def add_training_data(spoken_command1, spoken_command2, user_id, TrainingDictionary):
    fw = open(TrainingDataFile, 'wb')
    TrainingDictionary[user_id] = [spoken_command1, spoken_command2]
    pickle.dump(TrainingDictionary, fw)
    fw.close()

def load_training_data():
    fr = open(TrainingDataFile, 'rb')
    TrainingDictionary = pickle.load(fr)
    fr.close()
    return TrainingDictionary

def send_serial_data(command):
    try:
        ser = serial.Serial(serial_port)
        ser.write(command)
        ser.close()
    except Exception, inst:
        print "serial port can not be opened"
    
#def listen_from_user(spoken_command1, spoken_command2, user_id):

#def train_home(spoken_command1, spoken_command2, userid):

#def add_training_set(spoken_command1, spoken_command2, user_id):
    
#trd = load_training_data()
#print(trd)

#add_training_data('both', 'on', 'user2', trd)
    

def activate_home(spoken_command1, spoken_command2):
    global turn_off
    if ((spoken_command1 in light) and (spoken_command2 in on)):
       # print("I am calling ON.EXE")
      #  os.system("on.exe")
       # os.system("killon.exe")
        # print("SUCCESSFUL")
        print("The light is switched on")
        send_serial_data(light_on)
        speech.say("The light is switched on")
    elif ((spoken_command1 in light) and (spoken_command2 in off)):
        #print("I am calling OFF.EXE")
        #os.system("off.exe")
        #os.system("killon.exe")
        #print("SUCCESS")
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
        #listener.stoplistening()
        turn_off=1
        sys.exit()
        
    else:
        print("Sorry, This Command is not recognized by i-home")
        speech.say("Sorry This command is not recognized by i-home")
    


def callback(phrase, listener):
    print ": %s" % phrase
    print(phrase)
    global Mode
    global done
    global user_id
    
    if (phrase.lower() in personal):
        Mode = 'personal'
        #print(" I am in callback")
        #print(Mode)
        listener.stoplistening()
        done=1
    elif (phrase.lower() in default):
        Mode = 'default'
        #print(" I am in callback")
        #print(Mode)
        #listener.stoplistening()
        done=1   
    else:
        #print(phrase.split())
        spoken_input = phrase.split()
        #print(spoken_input)
        spoken_command1 = spoken_input[0].lower()
        spoken_command2 = spoken_input[len(spoken_input) - 1].lower()
        #print(spoken_command1)
        #print(spoken_command2)
        activate_home(spoken_command1, spoken_command2)
        TrainingDictionary = load_training_data()
        #user is new
        if (user_id not in TrainingDictionary):
            add_training_data(spoken_command1, spoken_command2, user_id, TrainingDictionary)

def initialize_home():
    global user_id
    user_id = pyfaces.recognize_face()
    print(user_id)
    #user_id = 'xyzxxxx'
    global Mode
    global done
    global turn_off
    TrainingDictionary = load_training_data()
    print(TrainingDictionary)
    if (user_id in TrainingDictionary):
        print("You have already visited i-home. The home is trained by your habit. Do you like the home to run in your personalized mode. say YES or NO")
        speech.say("You have already visited i-home. The home is trained by your habit. Do you like the home to run in your personalized mode. say YES or NO")
        listener = speech.listenforanything(callback)
        done=0
        while done!=1:
                continue            
        
        # it will go in while loop only when default mode is selected
        if Mode=='default':
            print 'in default mode'
            while listener.islistening():
                text = raw_input("> ")
                #text = 'asd'
                if turn_off==1:
                    sys.exit()
                elif text == "turn off":
                    listener.stoplistening()
                    sys.exit()
                else:
                    speech.say(text)
            #print(" I am outside the callback")
        #print(Mode)
        elif Mode=='personal':
            print 'in personal mode'
            spoken_command1 = TrainingDictionary[user_id][0]
            spoken_command2 = TrainingDictionary[user_id][1]
            #print(spoken_command1)
            #print(spoken_command2)
            activate_home(spoken_command1, spoken_command2)
    else:
        print 'New user found, set to defualt spoken mode'
        speech.say('New user found, set to defualt spoken mode')
        #for new user
        listener = speech.listenforanything(callback)
        # it will go in while loop only when default mode is selected
        while listener.islistening():
            text = raw_input("> ")
            if turn_off==1:
                    sys.exit()
              
            elif text == "turn off":
                listener.stoplistening()
                sys.exit()
            else:
                speech.say(text)

##print "Anything you type, speech will say back."
##print "Anything you say, speech will print out."
##print "Say or type 'turn off' to quit."
##print

print "i-home is activated"
#Mode = 'Default'
initialize_home()
##listener = speech.listenforanything(callback)
##
##
##while listener.islistening():
##    text = raw_input("> ")
##    if text == "turn off":
##        listener.stoplistening()
##        sys.exit()
##    else:
##        speech.say(text)





