import time
from microduino import sht2x

sensor = sht2x.SHT25(1)

while True:
    print("temperature: %0.2f" % sensor.getTemperature()+","+"humidity: %0.2f" % sensor.getHumidity())
    time.sleep(1)
