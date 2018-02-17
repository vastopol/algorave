#!/bin/bash

# time interval
LEN=0.1

# list of notes in scale
CHROMATIC=(C4 C#4 D4 E4 F4 F#4 G4 G#4 A4 A#4 B4)

sounder()
{
    for n in "${CHROMATIC[@]}";
    do
      echo $n
      /usr/bin/play -qn synth $1 sawtooth pluck $n repeat 2;
    done
}

sounder $LEN
