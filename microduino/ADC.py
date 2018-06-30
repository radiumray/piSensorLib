import time
import smbus

class ADC(object):
	ADDR = 0x12

	def __init__(self, address=ADDR):
		self._address = address
		self._bus = smbus.SMBus(1)

	def read(self, chn): #channel
		try:
			if chn == 0:
				self._bus.write_byte(self._address,0x40)
			if chn == 1:
				self._bus.write_byte(self._address,0x41)
			if chn == 2:
				self._bus.write_byte(self._address,0x42)
			if chn == 3:
				self._bus.write_byte(self._address,0x43)
			#self._bus.read_byte(self.ADDR) # dummy read to start conversion
		except Exception as e:
		    print ("Address: %s" % self._address)
		    print (e)
		return self._bus.read_byte(self._address)

	def write(self, val):
		try:
			temp = val # move string value to temp
			temp = int(temp) # change string to integer
			# print temp to see on terminal else comment out
			self._bus.write_byte_data(self._address, 0x40, temp)
		except Exception as e:
		    print ("Error: Device address: 0x%2X" % self._address)
		    print (e)
