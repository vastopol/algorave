#!/usr/bin/python

# Modules
import sox #??? not working properly
import sys
import subprocess
import time
import os
import itertools
#-------------------------------

# Global Variables
types = ['', 'pluck', 'sine', 'square', 'triangle', 'sawtooth', 'trapezium', 'exp', 'noise'] # synth types, 0 = empty where default is sine
notes = ['C4', 'C#4', 'D4', 'E4', 'F4', 'F#4', 'G4', 'G#4', 'A4', 'A#4', 'B4']      # chromatic scale in c (default)
synth = types[1] # current synth (user can change)
length = .1      # time interval for notes (user can change)
amount = 1       # number of times selected part is played (user can change)
#-------------------------------

def main(argv):
    global types,notes,synth,length,amount
    while True:
        listy = getargs()
        for i in listy:
            #print i[0]
            if i[0] == 'play':
                if len(i) == 1:
                    sox_play_scale(None) # default
                else:
                    i.pop(0)
                    i = map(str.upper,i)
                    sox_play_scale(i)
            elif i[0] == 'chord':
                if len(i) == 1:
                    sox_play_chord(None) # default
                else:
                    i.pop(0)
                    i = map(str.upper,i)
                    sox_play_chord(i)
            elif i[0] == 'time' and len(i) >1:
                if float(i[1]) >= 0:
                    length = float(i[1])
                else:
                    print("ERR time format: " + i[1])
            elif i[0] == 'amount' and len(i) >1:
                if int(i[1]) >= 1:
                    amount = int(i[1])
                else:
                    print("ERR amount format: " + i[1])
            elif i[0] == 'synth' and len(i) >1:
                if i[1] in types:
                    synth = i[1]
                else:
                    print("ERR unknown synth: " + i[1])
            elif i[0] == 'show':
                show()
            elif i[0] == 'stop':
                silence()
            elif i[0] == 'quit':
                quit()
            else:
                print("ERR unknown argument: ", i)
#-------------------------------

def getargs():
    line = raw_input("sox>> ")
    line2 = line.split(';')
    line3 = []
    line4 = []
    for i in line2:
        if len(i.strip()) != 0:
            line3.append(i.strip())
    for i in line3:
        line4.append(i.split())
    return line4
#-------------------------------

def show():
    print("current settings")
    print("synthesizer = " + synth)
    print("time length = " + str(length))
    print("repeat amount = " + str(amount))
#---------------------------------

def silence():
    subprocess.call('killall play',shell=True)
#---------------------------------

def quit():
    subprocess.call('killall play',shell=True)
    sys.exit(0)
#---------------------------------

# Wrapper
# var either None or list
def sox_play_scale(var):
    if var != None:
        for j in range(amount):
            for i in range(len(var)):
                # s = ['play -qn synth', str(length), synth, notes[i]] # str to be formated and filled in
                s = 'play -qn synth' + ' ' + str(length) + ' ' + synth + ' ' + var[i] # str to be formated and filled in
                print(var[i])
                player(s,0)
    else:
        for j in range(amount):
            for i in range(len(notes)):
                # s = ['play -qn synth', str(length), synth, notes[i]] # str to be formated and filled in
                s = 'play -qn synth' + ' ' + str(length) + ' ' + synth + ' ' + notes[i] # str to be formated and filled in
                print(notes[i])
                player(s,0)
#------------------------------


# Wrapper
# var either None or list
def sox_play_chord(var):
    if var != None:
        for j in range(amount):
            for i in range(len(var)):
                # s = ['play -qn synth', str(length), synth, notes[i]] # str to be formated and filled in
                s = 'play -qn synth' + ' ' + str(length) + ' ' + synth + ' ' + var[i] # str to be formated and filled in
                print(var[i])
                player(s,1)
    else:
        for j in range(amount):
            for i in range(len(notes)):
                # s = ['play -qn synth', str(length), synth, notes[i]] # str to be formated and filled in
                s = 'play -qn synth' + ' ' + str(length) + ' ' + synth + ' ' + notes[i] # str to be formated and filled in
                print(notes[i])
                player(s,1)
#------------------------------

# 0 = scale, 1 = chord
def player(sound,option=0):
    # OPTION 1
    # sox.core.play(sound) # doesnt work...
    # OPTION 2
    # proc = subprocess.Popen(sound,shell=True)
    # time.sleep(delays)
    # subprocess.call('pkill play',shell=True)
    # OPTION 3
    if option == 0:
        os.system(sound)
    elif option == 1:
        os.system(sound + ' ' + '&')
#---------------------------------

if __name__ == '__main__':
    main(sys.argv)
