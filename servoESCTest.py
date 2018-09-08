import time
from microduino import PWM
pwm =PWM.PWM(address=0x41)

pwm.set_pwm_freq(50)

'''
pwm.escControl(3,1500)
time.sleep(2)
print("init")
'''

while(True):
    pwm.escControl(3, 1200)
    time.sleep(1)
    print("forward")

    pwm.escControl(3, 1500)
    time.sleep(0.5)
    print("stop")

    pwm.servoTo(0, 50)
    for i in range(20,150,1):
        pwm.servoTo(0,i)
        time.sleep(0.1)
    for i in range(150,20,-1):
        pwm.servoTo(0,i)
        time.sleep(0.1)
    print("servo")

    pwm.escControl(3, 1800)
    time.sleep(1)
    print("backward")

    pwm.escControl(3, 1500)
    time.sleep(0.5)
    print("stop")




'''
import time
from microduino import PWM
pwm =PWM.PWM(address=0x41)
pwm.set_pwm_freq(50)
print('Moving servo on channel 0, press Ctrl-C to quit...')
pwm.servoTo(0,20)
while True:
    for i in range(20,150,1):
        pwm.servoTo(0,i)
        time.sleep(0.1)
    for i in range(150,20,-1):
        pwm.servoTo(0,i)
        time.sleep(0.1)
'''