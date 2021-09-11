from gpiozero import Servo
from time import sleep

myGPIO = 14
myCorrection = 0
maxPW = (2.0 + myCorrection) /1000
minPW = (1.0 - myCorrection) /1000
servo = Servo(myGPIO,min_pulse_width=minPW, max_pulse_width=maxPW)

while True:
	print('Set value range -1.0 to +0.0')
	for value in range(0,11,1):
		value2=(float(value)-10)/10
		servo.value=value2
		print(value2)
		sleep(0.1)
	print('Set value range +0.0 to -0.9')
	for value in range(11,20,1):
		value2=(float(value)-10)/10
		servo.value=value2
		print(value2)
		sleep(0.1)
	sleep(2)
