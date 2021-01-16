from time import sleep
import RPi.GPIO as GPIO
import math
import numpy as np

DIR = 20
STEP = 18
CW = 1
CCW= 0
SPR = 48

GPIO.setmode(GPIO.BCM)
GPIO.setup(DIR,GPIO.OUT)
GPIO.setup(STEP,GPIO.OUT)
GPIO.output(DIR, CW)

MODE = (14, 15, 18)
GPIO.setup(MODE,GPIO.OUT)
RESOLUTION = {'Full': (0,0,0),
              'Half': (1,0,0),
              '1/4':  (0,1,0),
              '1/8':  (1,1,0),
              '1/16': (0,0,1),
              '1/32': (1,0,1)}
#GPIO.output(MODE,RESOLUTION['1/32'])

step_count = SPR*32*32
step_count = 1000
delay = 0.0208/32/32/20
delay = 0.000001
delay = 0.02
delayVec=[]
amplitudeD = 100.
T = 1.
invOmega = 1/(2*math.pi/T)
delay = 0.0
y=0.0
for x in range(step_count):
#    delayVec.append(invOmega * (math.acos(x/math.pi*10/step_count) - math.acos(x+1)/math.pi*10/step_count))
    #delay = (math.acos(float(7)/math.pi*float(10)/float(step_count)))
    y= x+0.00000000000000001
    delay = ((np.cos((y/3.14*10/step_count*2))*0.5)+0.5)*0.01+0.000001
    print(str(x)+"   "+str(delay))
    delayVec.append(0.208)

#delay = 1

#for x in range(step_count):
#    GPIO.output(STEP, GPIO.HIGH)
#    sleep(delay)
#    GPIO.output(STEP, GPIO.LOW)
#    sleep(delay)

sleep(.5)

GPIO.output(DIR, CCW)
GPIO.output(14, GPIO.HIGH)

for x in range(step_count):
    GPIO.output(STEP, GPIO.HIGH)
    sleep(delayVec[x])
    GPIO.output(STEP, GPIO.LOW)
    sleep(delayVec[x])

