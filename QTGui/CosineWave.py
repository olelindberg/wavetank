from time import sleep

import numpy as np
import time
import StepperMotorUtil as smu
import TrackConstants as tc
import math

def runStepper(stroke,period,numPeriods):

    track       = tc.TrackConstants()
    Nx          = 21 
    halfperiod  = 0.5*period
    amplitude   = 0.5*stroke            # [m]
    angularFreq = 2.0*math.pi/period    # [rad/s]

    x,dx  = np.linspace(-amplitude,amplitude,Nx, retstep=True) # Maybe clustering toward the ends?
    x     = np.flip(x,axis=0) 
    t     = 1/angularFreq*np.arccos(x/amplitude)
    steps = int(dx/track.dx)

    Vector = []
    for i in range(Nx-1):
        freq = int(np.round(steps/(t[i+1]-t[i])))
        Vector.append([freq,steps])
   
    for n in range(numPeriods):
        
        smu.pi.write(smu.DIR,smu.FORWARD)
        smu.generate_ramp(Vector)
        sleep(halfperiod)

        smu.pi.write(smu.DIR,smu.BACKWARD)
        smu.generate_ramp(Vector)
        sleep(halfperiod)
    
    smu.pi.set_PWM_dutycycle(smu.STEP,0) #PWM off
    
    

