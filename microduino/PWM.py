#!/usr/bin/env python  
# -*- coding: utf-8 -*-

import logging
import time
import math
import smbus
import subprocess

# Registers/etc:
PCA9685_ADDRESS    = 0x41
MODE1              = 0x00
MODE2              = 0x01
SUBADR1            = 0x02
SUBADR2            = 0x03
SUBADR3            = 0x04
PRESCALE           = 0xFE
LED0_ON_L          = 0x06
LED0_ON_H          = 0x07
LED0_OFF_L         = 0x08
LED0_OFF_H         = 0x09
ALL_LED_ON_L       = 0xFA
ALL_LED_ON_H       = 0xFB
ALL_LED_OFF_L      = 0xFC
ALL_LED_OFF_H      = 0xFD

# Bits:
RESTART            = 0x80
SLEEP              = 0x10
ALLCALL            = 0x01
INVRT              = 0x10
OUTDRV             = 0x04

servo_min = 102
servo_max = 512
ESC_min = 208
ESC_max = 410

logger = logging.getLogger(__name__)

class PWM(object):

    def __init__(self, address=PCA9685_ADDRESS):
        try:
            self._address = address
            self._bus = smbus.SMBus(1)
            self.reset()
            self.set_pwm_freq(50)
            
        except (IOError):
            subprocess.call(['i2cdetect', '-y', '1'])
            print("IO Error")
            time.sleep(0.01)
            
    def reset(self):
        self._bus.write_byte_data(self._address, MODE1, RESTART)
        time.sleep(0.01)

    def set_pwm_freq(self, freq_hz):
        #Set the PWM frequency to the provided value in hertz.
        try:	
            freq_hz *=0.9
            prescaleval = 25000000.0    # 25MHz
            prescaleval /= 4096.0       # 12-bit
            prescaleval /= float(freq_hz)
            prescaleval -= 1.0
            logger.debug('Setting PWM frequency to {0} Hz'.format(freq_hz))
            logger.debug('Estimated pre-scale: {0}'.format(prescaleval))
            prescale = int(math.floor(prescaleval + 0.5))
            logger.debug('Final pre-scale: {0}'.format(prescale))
            oldmode = self._bus.read_byte_data(self._address,MODE1)
            newmode = (oldmode & 0x7F) | 0x10    # sleep
            self._bus.write_byte_data(self._address, MODE1, newmode)
            self._bus.write_byte_data(self._address, PRESCALE, prescale)
            self._bus.write_byte_data(self._address, MODE1, oldmode)
            time.sleep(0.01)
            self._bus.write_byte_data(self._address, MODE1, oldmode | 0xa0)
            time.sleep(0.01)
        except (IOError):
            subprocess.call(['i2cdetect', '-y', '1'])
            print("IO Error")
            time.sleep(0.01)

    def set_pwm(self, channel, on, off):
        #Sets a single PWM channel.
        try:
            pwmData = []
            pwmData.append(on)
            pwmData.append(on>>8)
            pwmData.append(off)
            pwmData.append(off>>8)
            self._bus.write_i2c_block_data(self._address,LED0_ON_L+4*channel, pwmData)
            #time.sleep(0.01)
        except (IOError):
            #subprocess.call(['i2cdetect', '-y', '1'])
            print("IO Error")
            time.sleep(0.01)
    '''
    def set_all_pwm(self, on, off):
        #Sets all PWM channels.
        try:
            self._bus.write_byte_data(self._address, ALL_LED_ON_L, on & 0xFF)
            self._bus.write_byte_data(self._address, ALL_LED_ON_H, on >> 8)
            self._bus.write_byte_data(self._address, ALL_LED_OFF_L, off & 0xFF)
            self._bus.write_byte_data(self._address, ALL_LED_OFF_H, off >> 8)
            time.sleep(0.01)
        except (IOError):
            print("IO Error")
            time.sleep(0.01)
    '''
    def constrain(self, val, min_val, max_val):
        if val < min_val:
            return min_val
        if val > max_val:
            return max_val
        return val

    def mapTo(self, x, in_min, in_max, out_min, out_max):
        return int((x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min)

    def servoTo(self, channel, degree):
        toDegree =self.constrain(degree, 0, 180)
        toDegree = self.mapTo(toDegree, 0, 180 ,servo_min, servo_max)
        self.set_pwm(channel, 0, toDegree)
        
    def escControl(self, channel, escValue):
        toESC =self.constrain(escValue, 1000, 2000)
        toESC = self.mapTo(toESC, 1000, 2000 ,ESC_min, ESC_max)
        self.set_pwm(channel, 0, toESC)

