#!/usr/bin/env python  
# -*- coding: utf-8 -*-

import time
import smbus

class DOTMATRIX(object):
    rowColBGR=bytearray(5)

    def __init__(self, address=0x40):
            self._address = address
            self._bus = smbus.SMBus(1)

    def setLedColor(self, x,y,r,g,b):
        self.rowColBGR[0]=x
        self.rowColBGR[1]=y
        self.rowColBGR[2]=b
        self.rowColBGR[3]=g
        self.rowColBGR[4]=r

        temp = bytearray(4)
        temp[0] = 0x80 | (self.rowColBGR[0] << 3) | self.rowColBGR[1]
        temp[1] = int(self.rowColBGR[2] / 8)
        temp[2] = 0x20 | int(self.rowColBGR[3] / 8)
        temp[3] = 0x40 | int(self.rowColBGR[4] / 8)

        try:
            for i in range(4):
                self._bus.write_byte(self._address, temp[i])
        except (IOError):
            print("IO Error")
            time.sleep(0.01)

    def clearDisplay(self):
        try:
            self._bus.write_byte(self._address, 0x60)
        except (IOError):
            print("IO Error")
            time.sleep(0.01)        
