# -*- coding: utf-8 -*-
"""
Created on Sat Apr 15 02:18:49 2017

@author: kusha
"""

import time
import serial 
def output():
    usbport="COM4"
    ser=serial.Serial("COM4", 9600, timeout=1)
    time.sleep(1)
    ser.setDTR(level=0)
    time.sleep(1)
    ticks=time.time();
    
    ser.write("1")
     
        
    
    while(time.time()-ticks<=4):
        None;
    ser.write('0')    
 
    ser.close()
    
if __name__ == "__main__":
    output()
    


