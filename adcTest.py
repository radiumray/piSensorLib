import time
from microduino import ADC

sensor = ADC.ADC(0x12)

while True:
    print ('AIN0 = ', sensor.read(0))
    print ('AIN1 = ', sensor.read(1))
    print ('AIN2 = ', sensor.read(2))
    print ('AIN3 = ', sensor.read(3))
    print ('---------------------')
    time.sleep(1)


'''
import smbus
import time
# for RPI version 1, use "bus = smbus.SMBus(0)"
bus = smbus.SMBus(1)
#check your PCF8591 address by type in 'sudo i2cdetect -y -1' in terminal.
def setup(Addr):
    global address
    address = Addr
def read(chn): #channel
    #try:
    if chn == 0:
        bus.write_byte(address,0x40)
    if chn == 1:
        bus.write_byte(address,0x41)
    if chn == 2:
        bus.write_byte(address,0x42)
    if chn == 3:
        bus.write_byte(address,0x43)
        bus.read_byte(address) # dummy read to start conversion
    #except Exception, e:
    #    print "Address: %s" % address
    #    print e
    return bus.read_byte(address)

def write(val):
    #try:
    temp = val # move string value to temp
    temp = int(temp) # change string to integer
    # print temp to see on terminal else comment out
    bus.write_byte_data(address, 0x40, temp)
    #except Exception, e:
    #    print "Error: Device address: 0x%2X" % address
    #    print e
 
if __name__ == "__main__":
    setup(0x12)
    while True:
        print ('AIN0 = ', read(0))
        print ('AIN1 = ', read(1))
        print ('AIN2 = ', read(2))
        print ('AIN3 = ', read(3))
        print (' ')
        tmp = read(0)
        tmp = tmp*(255-125)/255+125 # LED won't light up below 125, so convert '0-255' to '125-255'
        write(tmp)
        time.sleep(1.0)
'''


'''
#!/usr/bin/env python
import time
#board pins
#pin 3=SDA
#pin 5=SCL

from smbus import SMBus

bus = SMBus(1)
temp_pin=0
light_pin=1


def read_ain(i):    
    global bus
    bus.write_byte(0x48, i)
    bus.read_byte(0x48)#first 2 are last state, and last state repeated.
    bus.read_byte(0x48)
    return bus.read_byte(0x48)

while(True):
    print (read_ain(0))
    print (read_ain(1))
    print ("---")
    #print get_temp()
    #print get_light_level()
    time.sleep(3)#sec
'''