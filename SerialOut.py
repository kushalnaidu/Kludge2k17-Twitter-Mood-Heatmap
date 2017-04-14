# -*- coding: utf-8 -*-
"""
Created on Sat Apr 15 02:18:49 2017

@author: kusha
"""

import time
import serial 
def output():
    usbport="COM3"
    ser=serial.Serial(usbport, 9600, timeout=1)
    ticks=time.time();
    ser.write('1')
    while(time.time()-ticks<=2):
        print "Waiitng"
        None;
    ser.write('0')    
 
    
    