from time import sleep

import numpy as np
import time
import StepperMotorUtil as smu
import TrackConstants as tc

def runStepper(direction):

    track      = tc.TrackConstants()
    halfperiod = 0.25
    stroke     = 0.1*track.length         # [m]
    steps      = int(stroke/track.dx)
    freq       = int(steps/halfperiod) # [1/s]

    smu.pi.write(smu.DIR,direction)
    smu.generate_ramp([[freq,steps]])
    sleep(halfperiod)
    
    smu.pi.set_PWM_dutycycle(smu.STEP,0) #PWM off
    
    

