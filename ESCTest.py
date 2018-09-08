#!/usr/bin/python

'''
import RPi.GPIO as GPIO
import time
import sys

motor_pin = 13

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

GPIO.setup(motor_pin, GPIO.OUT)
motor = GPIO.PWM(motor_pin, 50)

motor.start(7.5)
time.sleep(3)
print("init")

motor.ChangeDutyCycle(7)
time.sleep(1)
print("forward")

motor.ChangeDutyCycle(78)
time.sleep(1)
print("backward")

motor.stop()
'''







'''
import RPi.GPIO as GPIO
from time import sleep
import pigpio

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

# Connect to pigpio
pi = pigpio.pi()

# Calibrate ESC
ESC_GPIO = 13
pi.set_servo_pulsewidth(ESC_GPIO, 2000) # Maximum throttle.
sleep(2)
pi.set_servo_pulsewidth(ESC_GPIO, 1000) # Minimum throttle.
sleep(2)

#pi.set_servo_pulsewidth(ESC_GPIO, speed * 1000 / 7 + 1000)
'''



'''
import time
from microduino import PWM

pwm =PWM.PWM(address=0x41)

# Set frequency to 60hz, good for servos.
#pwm.set_pwm_freq(60)
pwm.set_pwm_freq(50)

while True:
    for i in range(180):
        pwm.servoTo(0, i)
        time.sleep(0.01)
    for i in range(180,0,-1):
         pwm.servoTo(0, i)
         time.sleep(0.01)
'''



import time
from microduino import PWM
pwm =PWM.PWM(address=0x41)

# Set frequency to 60hz, good for servos.
pwm.set_pwm_freq(50)
'''
pwm.set_pwm(3, 0, 306)
time.sleep(0.5)
print("init")
pwm.set_pwm(3, 0, 306)
time.sleep(0.5)
print("init")
'''
pwm.set_pwm(3, 0, 320)
time.sleep(1)
print("forward")

pwm.set_pwm(3, 0, 306)
time.sleep(0.5)
print("stop")
pwm.set_pwm(3, 0, 306)
time.sleep(0.5)
print("stop")

pwm.set_pwm(3, 0, 280)
time.sleep(1)
print("backward")

pwm.set_pwm(3, 0, 306)
time.sleep(0.5)
print("stop")
pwm.set_pwm(3, 0, 306)
time.sleep(0.5)
print("stop")

