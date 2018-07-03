# piSensorLib


## Microduino树莓派扩展板传感器库


### 硬件提供接口：
+ ADC：ADC1, ADC2, ADC3, ADC4, 
+ I2C:
+ UART:
+ GPIO:IO12, IO13, IO16,
+ TFT:
+ I2S:


### 库安装：
+ LX终端,进入文件夹：输入 sudo sh ./install.sh

### 卸载：
+ LX终端,进入文件夹：输入 sudo sh ./uninstall.sh


### 示例：
+ adcTest.py  ADC测试
+ adcControlServo.py  ADC显示,舵机测试
+ gpioTest.py   GPIO测试
+ lm75Test.py  LM75测试
+ servoTest.py  舵机测试
+ tempHumi.py   温湿度测试
> + 彩灯控制:参见 https://learn.adafruit.com/neopixels-on-raspberry-pi/software
+ 需要编译和安装 rpi_ws281x 库(只支持python2)

### 参考URL：
https://www.sunfounder.com/learn/category/sensor-kit-v2-0-for-raspberry-pi-b-plus.html
