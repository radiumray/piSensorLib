import time
from microduino import ADC,PWM

sensor = ADC.ADC(0x12)
pwm =PWM.PWM(address=0x41)

# Configure min and max servo pulse lengths
servo_min = 130  # Min pulse length out of 4096
servo_max = 600  # Max pulse length out of 4096

# Set frequency to 60hz, good for servos.
pwm.set_pwm_freq(60)

senVal=sensor.read(0)
print ('AIN1 = ', senVal)

while True:
    for i in range(180):
        pwm.servoTo(0, i)
        time.sleep(0.01)
    for i in range(180,0,-1):
         pwm.servoTo(0, i)
         time.sleep(0.01)