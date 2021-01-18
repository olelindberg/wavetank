from time import sleep

import numpy as np
import time
import StepperMotorUtil as smu
import TrackConstants as tc

def runStepper(stroke,period,numPeriods):

    track      = tc.TrackConstants()
    halfperiod = 0.5*period            # [s]
    steps      = int(stroke/track.dx)
    freq       = int(steps/halfperiod) # [1/s]

    Vector = [[freq,steps]] 
   
    for n in range(numPeriods):
        
        smu.pi.write(smu.DIR,smu.FORWARD)
        smu.generate_ramp(Vector)
        sleep(halfperiod)

        smu.pi.write(smu.DIR,smu.BACKWARD)
        smu.generate_ramp(Vector)
        sleep(halfperiod)
    
    smu.pi.set_PWM_dutycycle(smu.STEP,0) #PWM off
    
    

