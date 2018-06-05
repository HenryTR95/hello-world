import subprocess
import serial 
import time

ser = 0

#subprocess.call('python grabserial')

#LED_index = input("what LED?")


def init_serial():
	#COMNUM = 1
	global ser
	ser = serial.Serial('/dev/ttyACM1', 9600)
	#ser.baudrate = 9600
	#ser.port = '/dev/ttyACM1'
	#ser.timeout = 1000000
	if ser.isOpen():
		print 'Open: ' + ser.portstr
	
#subprocess.call('ls')

init_serial()

# wait for arduino serial com
time.sleep(0.5)

while 1:
	temp = raw_input('Make motor move forward or backward: ')
	ser.write(temp)
	#bytes = ser.readline()
	#print bytes 

bytes = ser.readline()
print bytes 
	
ser.close()

