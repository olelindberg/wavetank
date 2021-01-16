from time import sleep
import pigpio

DIR = 15     # Direction GPIO Pin
STEP = 21    # Step GPIO Pin
SWITCH = 16  # GPIO pin of switch

# Connect to pigpiod daemon
pi = pigpio.pi()

# Set up pins as an output
pi.set_mode(DIR, pigpio.OUTPUT)
pi.set_mode(STEP, pigpio.OUTPUT)

# Set up input switch
pi.set_mode(SWITCH, pigpio.INPUT)
pi.set_pull_up_down(SWITCH, pigpio.PUD_UP)

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
        x = steps & 255
        y = steps >> 8
        chain += [255, 0, wid[i], 255, 1, x, y]

    pi.wave_chain(chain)  # Transmit chain.


MODE = (14, 15, 18)   # Microstep Resolution GPIO Pins
RESOLUTION = {'Full': (0, 0, 0),
              'Half': (1, 0, 0),
              '1/4': (0, 1, 0),
              '1/8': (1, 1, 0),
              '1/16': (0, 0, 1),
              '1/32': (1, 0, 1)}
for i in range(3):
    pi.write(MODE[i], RESOLUTION['Full'][i])

# Set duty cycle and frequency
#pi.set_PWM_dutycycle(STEP, 128)  # PWM 1/2 On 1/2 Off
#pi.set_PWM_frequency(STEP, 32000)  # 500 pulses per second
try:
    pi.write(14, 1)  # Set direction
    pi.write(DIR, 0)  # Set direction
    # Ramp up
    generate_ramp([[500, 50],
               [1192, 119],
               [2377, 237],
               [3547, 354],
               [4694, 469],
               [5812, 581],
               [6892, 689],
               [7930, 733],
               [8917, 891],
               [9847, 985],
               [10716, 1071],
               [11516, 1151],
               [12244, 1224],
               [12894, 1289],
               [13462, 1346],
               [13945, 1395],
               [14340, 1434],
               [14645, 1464],
               [14856, 1485],
               [14974, 14970]])
#               [14996, 1499]])
    sleep(2)
    pi.write(DIR, 0)  # Set direction
    generate_ramp([[14924, 1494],
               [14757, 1475],
               [14497, 14497],
               [14146, 1415],
               [13704, 1370],
               [13176, 1317],
               [12565, 1256],
               [11874, 1187],
               [11107, 1110],
               [10271, 1027],
               [9369, 937],
               [8409, 841],
               [7395, 739],
               [6334, 633],
               [5233, 523],
               [4099, 409],
               [2939, 294],
               [1760, 176],
               [570, 57]])
    sleep(2)

    pi.write(DIR, 1)  # Set direction
    # Ramp up
    generate_ramp([[500, 50],
               [1192, 119],
               [2377, 237],
               [3547, 354],
               [4694, 469],
               [5812, 581],
               [6892, 689],
               [7930, 733],
               [8917, 891],
               [9847, 985],
               [10716, 1071],
               [11516, 1151],
               [12244, 1224],
               [12894, 1289],
               [13462, 1346],
               [13945, 1395],
               [14340, 1434],
               [14645, 1464],
               [14856, 1485],
               [14974, 14970]])
#               [14996, 1499]])
    sleep(2)
    pi.write(DIR, 0)  # Set direction
    generate_ramp([[14924, 1494],
               [14757, 1475],
               [14497, 14497],
               [14146, 1415],
               [13704, 1370],
               [13176, 1317],
               [12565, 1256],
               [11874, 1187],
               [11107, 1110],
               [10271, 1027],
               [9369, 937],
               [8409, 841],
               [7395, 739],
               [6334, 633],
               [5233, 523],
               [4099, 409],
               [2939, 294],
               [1760, 176],
               [570, 57]])
    



except KeyboardInterrupt:
    print "\nCtrl-C pressed.  Stopping PIGPIO and exiting..."
    pi.set_PWM_dutycycle(STEP, 0)
finally:
    pi.set_PWM_dutycycle(STEP, 0)

try:
    while True:
        pi.write(DIR, pi.read(SWITCH))  # Set direction
        sleep(.1)

except KeyboardInterrupt:
    print ("\nCtrl-C pressed.  Stopping PIGPIO and exiting...")
finally:
    pi.set_PWM_dutycycle(STEP, 0)  # PWM off
    pi.stop()
