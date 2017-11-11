#!/usr/bin/python

# Modules
import sox #??? not working properly
import sys
import subprocess
import time
#-------------------------------

# Global Variables
types = ['', 'pluck', 'sine', 'square', 'triangle', 'sawtooth', 'trapezium', 'exp'] # synth types, 0 = empty where default is sine
notes = ['C4', 'C#4', 'D4', 'E4', 'F4', 'F#4', 'G4', 'G#4', 'A4', 'A#4', 'B4']      # chromatic scale in c
synth = types[1] # current synth
length = .1      # time interval for notes
delays = .2      # time to sleep between notes
#-------------------------------

def main(argv):
    global types,notes,synth,length,delays
    while True:
        listy = getargs()
        for i in listy:
            print i
        for i in listy:
            print i[0]
            if i[0] == 'time' and len(i) >1:
                delays = float(i[1])
            elif i[0] == 'synth' and len(i) >1:
                synth = i[1]
            elif i[0] == 'show':
                show()
            elif i[0] == 'stop':
                silence()
            elif i[0] == 'quit':
                quit()
            else:
                print("ERR unknown argument: ", i)
        sox_play()
#-------------------------------

def getargs():
    line = raw_input()
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
    for j in range(2):
        for i in range(len(notes)):
            s = ['play -qn synth', str(length), synth, notes[i]] # str to be formated and filled in
            print(notes[i])
            player(s)
#------------------------------

def player(sound):
    # sox.core.play(sound) # doesnt work...
    proc = subprocess.Popen(sound,shell=True)
    time.sleep(delays)
    subprocess.call('pkill play',shell=True)
#---------------------------------

def show():
    print("current settings")
    print("synthesizer = " + synth)
    print("time delay = " + str(delays))
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
