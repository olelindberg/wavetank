from time import sleep
import pigpio
import numpy as np

DIR = 17     # Direction GPIO Pin
STEP = 4    # Step GPIO Pin
SWITCH = 16  # GPIO pin of switch

# Connect to pigpiod daemon
pi = pigpio.pi()

# Set up pins as an output
pi.set_mode(DIR, pigpio.OUTPUT)
pi.set_mode(STEP, pigpio.OUTPUT)

# Set up input switch
pi.set_mode(SWITCH, pigpio.INPUT)
pi.set_pull_up_down(SWITCH, pigpio.PUD_UP)

MODE = (14, 15, 18)   # Microstep Resolution GPIO Pins
RESOLUTION = {'Full': (0, 0, 0),
              'Half': (1, 0, 0),
              '1/4': (0, 1, 0),
              '1/8': (1, 1, 0),
              '1/16': (0, 0, 1),
              '1/32': (1, 0, 1)}
for i in range(3):
    pi.write(MODE[i], RESOLUTION['Full'][i])

pi.write(14, 1)  # Set direction
# Set duty cycle and frequency
#pi.set_PWM_dutycycle(STEP, 128)  # PWM 1/2 On 1/2 Off
#pi.set_PWM_frequency(STEP, 500)  # 500 pulses per second

def generate_ramp(ramp):
    """Generate ramp wave forms.
    ramp:  List of [Frequency, Steps]
    """
    pi.wave_clear()     # clear existing waves
    length = len(ramp)  # number of ramp levels
    wid = [-1] * length

    # Generate a wave per ramp level
    for i in range(length):
        frequency = ramp[i][0]
        micros = int(500000 / frequency)
        wf = []
        wf.append(pigpio.pulse(1 << STEP, 0, micros))  # pulse on
        wf.append(pigpio.pulse(0, 1 << STEP, micros))  # pulse off
        pi.wave_add_generic(wf)
        wid[i] = pi.wave_create()

    # Generate a chain of waves
    chain = []
    for i in range(length):
        steps = ramp[i][1]
        x = int(steps) & 255
        y = int(steps) >> 8
        chain += [255, 0, wid[i], 255, 1, x, y]

    pi.wave_chain(chain)  # Transmit chain.

# Ramp up

def runStepper():
    len1 = 20
    Vector = []
    VectorBack = []
    for x in range(len1):
        Vector.append([0,0])
        VectorBack.append([0,0])
        #Vector[x].append([0,0])
    for x in range(len1):
        val = np.sin((x+1)/np.pi/(len1+1)*10/2)*15000
        Vector[x][0] = val.astype(int)
        Vector[x][1] = val.astype(int)/25
        val = np.sin(((x+len1)+1)/np.pi/(len1+1)*10/2)*15000
        VectorBack[x][0] = val.astype(int)
        VectorBack[x][1] = Vector[x][1]

    pi.write(DIR,0)
    generate_ramp(Vector)
    sleep(0.78)
    generate_ramp(VectorBack)
    sleep(0.78)

    pi.write(DIR, 1)  # Set directio
    generate_ramp([[1,1]])
    sleep(0.1)

    generate_ramp(Vector)
    sleep(0.78)
    generate_ramp(VectorBack)
    sleep(0.78)
    generate_ramp([[100,0]])
    sleep(0.5)
    pi.set_PWM_dutycycle(STEP,0) #PWM off 

#runStepper()
#try:
#    while True:
#        #pi.write(DIR, pi.read(SWITCH))  # Set direction
#        sleep(.1)

#except KeyboardInterrupt:
#    print ("\nCtrl-C pressed.  Stopping PIGPIO and exiting...")
#finally:
#    pi.set_PWM_dutycycle(STEP, 0)  # PWM off
#    pi.stop()


