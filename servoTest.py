import time

# Import the PWM module.
from microduino import PWM

# Alternatively specify a different address and/or bus:
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

