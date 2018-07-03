import random
from microduino import DOTMATRIX
import time

dotMat = DOTMATRIX.DOTMATRIX(0x40)

dotMat.setLedColor(1,1,255,0,255)
time.sleep(1)

dotMat.setLedColor(3,3,0,255,0)
time.sleep(1)

dotMat.clearDisplay()

while(True):
    for x in range(8):
        for y in range(8):
            r=int(random.randint(0,255))
            g=int(random.randint(0,255))
            b=int(random.randint(0,255))
            dotMat.setLedColor(x,y,r,g,b)
    time.sleep(1)
    dotMat.clearDisplay()
    time.sleep(1)



