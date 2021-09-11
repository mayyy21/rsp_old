import RPi.GPIO as GPIO
from time import sleep

def tonum(num):
	fm=10.0/180
	num=num*fm+2.5
	num=int(num*10)/10.0
	return num

servopin1=14
servopin2=15

GPIO.setmode(GPIO.BCM)
GPIO.setup(servopin1,GPIO.OUT,initial=False)
GPIO.setup(servopin2,GPIO.OUT,initial=False)
p1=GPIO.PWM(servopin1,50)
p2=GPIO.PWM(servopin2,50)

p1.start(tonum(0))
p2.start(tonum(0))
sleep(0.5)
p1.ChangeDutyCycle(0)
p2.ChangeDutyCycle(0)
sleep(0.1)

a=0
c=0
b=0
d=4

q=[0,10,20,30,40,50,60,70,80,90,100,110,120,130,140,150,160,170,180]
def left():
	global a,c
	a+=1
	for r in range(0, 19, 1):
		g=q[r]
		print('now angle: ',g)
		p1.ChangeDutyCycle(tonum(g))
		p2.ChangeDutyCycle(tonum(g))
		sleep(0.1)
		p1.ChangeDutyCycle(0)
		p2.ChangeDutyCycle(0)
		sleep(0.01)
'''	if c>2:
		c=c-1
		g=q[c]
		print('now angle: ',g)
		p1.ChangeDutyCycle(tonum(g))
		p2.ChangeDutyCycle(tonum(g))
		sleep(0.1)
		p1.ChangeDutyCycle(0)
		p2.ChangeDutyCycle(0)
		sleep(0.01)
	else:
		print('out of range')
		c=9
		g=85
		p1.ChangeDutyCycle(tonum(g))
		p2.ChangeDutyCycle(tonum(g))
		sleep(0.1)
		p1.ChangeDutyCycle(0)
		p2.ChangeDutyCycle(0)

		sleep(0.01)
'''

def right():
	global a,c
	for r in range(18,-1,-1):
		g=q[r]
		print('now angle: ',g)
		p1.ChangeDutyCycle(tonum(g))
		p2.ChangeDutyCycle(tonum(g))
		sleep(0.1)
		p1.ChangeDutyCycle(0)
		p2.ChangeDutyCycle(0)
		sleep(0.01)
'''	if c<16:
		c=c+1
		g=q[c]
		print('now angle: ',g)
		p1.ChangeDutyCycle(tonum(g))
		p2.ChangeDutyCycle(tonum(g))
		sleep(0.1)
		p1.ChangeDutyCycle(0)
		p2.ChangeDutyCycle(0)
		sleep(0.01)
	else:
		print('out of range')
		c=9
		g=85
		p1.ChangeDutyCycle(tonum(g))
		p2.ChangeDutyCycle(tonum(g))
		sleep(0.1)
		p1.ChangeDutyCycle(0)
		p2.ChangeDutyCycle(0)
		sleep(0.01)
'''
if __name__=='__main__':
	while True:
		left()
		sleep(1)
		right()
		sleep(3)
'''		x=input('input:')
		if x=='a':
			left()
		elif x=='d':
			right()

'''
