from gpiozero import LED
from time import sleep

led = LED(17)
print('hhhhhh')

while True:
    led.on()
    sleep(1)
    led.off()
    sleep(1)