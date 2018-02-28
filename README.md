# soxbox
command line synthesizer project

* dependencies
  * sox - cross-platform audio editing software (version 14.4.2)

To install SoX on Linux:
apt-get install sox

this project uses python 2.7 for now.

http://sox.sourceforge.net/sox.html

https://linux.die.net/man/1/sox

---------------------------------------

Plans:
- convert source from python2.7 to python3
- configure modules properly
- add feature to generate an output file as mp3, wav, etc... ???

---------------------------------------

bugs ???

try commands:

Fails:
chord c
chord c;

scale c
scale c;

Pass:
chord c c;
chord c c

scale c c;
scale c c
