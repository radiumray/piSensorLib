import time
from microduino import LM75
lm = LM75.LM75(1,0x48,1)

for x in range(0,10):
        temperature = lm.getTemp()
        print("temperature: %0.2f" % temperature)
        time.sleep(2)

