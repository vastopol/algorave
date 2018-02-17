#!/bin/bash

# Based on example:
# Steve Reich - Piano Phase; interpreter: Bourne-Again Shell
# http://www.commandlinefu.com/commands/view/20748/steve-reich-piano-phase-interpreter-bourne-again-shell

phase()
{
    while true;
    do
        for n in E4 F#4 B4 C#5 D5 F#4 E4 C#5 B4 F#4 D5 C#5;
        do
          /usr/bin/play -qn synth $1 pluck $n
        done
        echo -n "[$1]"
    done
}

phase 0.13 &
phase 0.131 &
