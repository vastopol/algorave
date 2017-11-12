#!/usr/bin/python

# Modules
import sox #??? not working properly
import sys
import subprocess
import time
import os
#-------------------------------

# Global Variables
types = ['', 'pluck', 'sine', 'square', 'triangle', 'sawtooth', 'trapezium', 'exp', 'noise'] # synth types, 0 = empty where default is sine
notes = ['C4', 'C#4', 'D4', 'E4', 'F4', 'F#4', 'G4', 'G#4', 'A4', 'A#4', 'B4']      # chromatic scale in c
synth = types[1] # current synth (user can change)
length = .2      # time interval for notes (user can change)
amount = 1       # number of times selected part is played (user can change)
#-------------------------------

def main(argv):
    global types,notes,synth,length,amount
    while True:
        listy = getargs()
        for i in listy:
            print i[0]
            if i[0] == 'play':
                sox_play()
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

def sox_play():
    for j in range(amount):
        for i in range(len(notes)):
            # s = ['play -qn synth', str(length), synth, notes[i]] # str to be formated and filled in
            s = 'play -qn synth' + ' ' + str(length) + ' ' + synth + ' ' + notes[i] # str to be formated and filled in
            print(notes[i])
            player(s)
#------------------------------

def player(sound):
    # OPTION 1
    # sox.core.play(sound) # doesnt work...
    # OPTION 2
    # proc = subprocess.Popen(sound,shell=True)
    # time.sleep(delays)
    # subprocess.call('pkill play',shell=True)
    # OPTION 3
    os.system(sound)
#---------------------------------

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
    sys.exit(0)
#---------------------------------

if __name__ == '__main__':
    main(sys.argv)
#-------------------------------
