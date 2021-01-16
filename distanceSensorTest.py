import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)

TRIG = 23
ECHO = 24

print("distance Measurement in Progress")

GPIO.setup(TRIG,GPIO.OUT)
GPIO.setup(ECHO,GPIO.IN)

GPIO.output(TRIG, False)

print("Waiting for Sensor to Settle")
time.sleep(2)

GPIO.output(TRIG, True)
time.sleep(0.00001)
GPIO.output(TRIG, False)
i = 0
succesBool = False
while GPIO.input(ECHO)==0:
    pulse_start = time.time()
    i += 1
    if i == 3:
        pulse_end = 0
        pulse_start = 1.715171572 
        succesBool = True
        break
i = 0
if succesBool
    while GPIO.input(EXHO)==1:
        pulse_end = time.time()
        i += 1;
        if i == 3:
            succesBool = True
            pulse_end = 0
            pulse_start = 1.715171572 


pulse_duration = pulse_end - pulse_start

distance = pulse_duration * 17150

distance = round(distance, 2)

print("Distance: ",distance," cm")

GPIO.cleanup()

