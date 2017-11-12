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
dictate = {}     # dictionary to save notes
#-------------------------------

def main(argv):
    global types,notes,synth,length,amount,dictate
    while True:
        listy = getargs()
        for i in listy:
            #print i[0]
            if i[0] == 'save':
                i.pop(0)
                if len(i) < 2:
                    print("ERR save format")
                else:
                    bop = i.pop(0)
                    dictate[bop] = i
            elif i[0] == 'scale':
                if len(i) == 1:
                    sox_play(None,0) # default
                elif len(i) == 2:
                    i.pop(0)
                    temp = map(str.upper,dictate[i[0]])
                    sox_play(temp,0) # default
                else:
                    i.pop(0)
                    i = map(str.upper,i)
                    sox_play(i,0)
            elif i[0] == 'chord':
                if len(i) == 1:
                    sox_play(None,1) # default
                elif len(i) == 2:
                    i.pop(0)
                    temp = map(str.upper,dictate[i[0]])
                    sox_play(temp,1) # default
                else:
                    i.pop(0)
                    i = map(str.upper,i)
                    sox_play(i,1)
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
            elif i[0] == 'reset':
                synth = types[1]
                length = .1
                amount = 1
                dictate = {}
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
    if len(dictate) > 0:
        print("saved items")
        for i in dictate:
            print(i + ' ' + str(dictate[i]))
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
# choice 0 = scale, 1 = chord
def sox_play(var,choice):
    if var == None:
        var = notes
    for j in range(amount):
        for i in range(len(var)):
            s = 'play -qn synth' + ' ' + str(length) + ' ' + synth + ' ' + var[i] # str to be formated and filled in
            print(var[i])
            player(s,choice)
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
