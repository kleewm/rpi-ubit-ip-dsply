#!/usr/bin/python3
#
# dsply-ubit adaptorMAC ubitMAC msg
#
# this works only on python3
# run the following to load bluezero module
# sudo pip3 install bluezero
# install bluezero code into MicroBit
# https://ukbaz.github.io/howto/ubit_workshop.html
#
# store in /home/pi and remember to chmod +x dsply-ubit
#
# kenneth@ec1213.net
# apr 2018


import time
import sys
import subprocess
from string import *
from bluezero import microbit

ctrlMAC = sys.argv[1]
ubitMAC = sys.argv[2]
my_text = sys.argv[3]

ubit = microbit.Microbit(adapter_addr=sys.argv[1],
                         device_addr=sys.argv[2])

#ubit = microbit.Microbit(adapter_addr='B8:27:EB:7F:95:64',
#                         device_addr='D5:14:E7:86:8C:D9')

ubit.connect()
looping = True
count2 = 0
while (looping and (count2 < 10)):
    ubit.text = my_text
    count = 0
    count2 = count2 + 1
    while ((count < 11) and looping):
       if ubit.button_a > 0:
          looping = False
          ubit.text = "A"
       if ubit.button_b > 0:
          looping = False
          ubit.text = "B"
       time.sleep(1)
       count = count + 1

ubit.disconnect()
