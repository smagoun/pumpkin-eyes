# Control code for creepy pumpkin eyes.
#
# Based on Adafruit Itsy Bitsy M0 Express IO demo

import board
import time
import gc
import random
from digitalio import DigitalInOut, Direction, Pull
import pulseio
import adafruit_dotstar
from adafruit_motor import servo

FREQ=50
ANGLE_MIN=0
ANGLE_MAX=180
ANGLE_MIDPOINT=90

# One pixel connected internally!
dot = adafruit_dotstar.DotStar(board.APA102_SCK, board.APA102_MOSI, 1, brightness=0.5)

# Built in red LED. Conflicts with servo on D13 below
# led = DigitalInOut(board.D13)
# led.direction = Direction.OUTPUT

# Global state
running = True
staring = False

# Button to toggle between run and standby (servos back to midpoint)
button = DigitalInOut(board.D0)
button.direction = Direction.INPUT
button.pull = Pull.UP

# Pin numbers and ordering figured out by a bit of trial and error
servo1 = servo.Servo(pulseio.PWMOut(board.D10, frequency=FREQ))
servo2 = servo.Servo(pulseio.PWMOut(board.D1, frequency=FREQ))
servo3 = servo.Servo(pulseio.PWMOut(board.D2, frequency=FREQ))
servo4 = servo.Servo(pulseio.PWMOut(board.D3, frequency=FREQ))
servo5 = servo.Servo(pulseio.PWMOut(board.D5, frequency=FREQ))
servo6 = servo.Servo(pulseio.PWMOut(board.D7, frequency=FREQ))
servo7 = servo.Servo(pulseio.PWMOut(board.D9, frequency=FREQ))
servo8 = servo.Servo(pulseio.PWMOut(board.D11, frequency=FREQ))
servo9 = servo.Servo(pulseio.PWMOut(board.D13, frequency=FREQ))   # Side effect, controls LED
servo10 = servo.Servo(pulseio.PWMOut(board.SCK, frequency=FREQ))
servo11 = servo.Servo(pulseio.PWMOut(board.SCL, frequency=FREQ))
# Can't figure out how to get a 12th PWM, so piggyback servo 12 on some other servo's pin
# servo12 = servo.Servo(pulseio.PWMOut(board.A2, frequency=FREQ))


######################### HELPERS ##############################

def randomOrange():
    '''Generate a random orange-ish color, like a flame'''
    r = random.randint(50, 200)
    g = random.randint(0, 80)   # If changing this, beware of overflow on the next line
    r = r if r > g else g + 20
    b = 0
    return [r, g, b]

def flicker(dot):
    '''Change color + brightness. Assumes a single DotStar'''
    dot[0] = randomOrange()
    dot.brightness = random.random()

def checkButton():
    '''Toggle the 'running' global on button press'''
    if (not button.value):  # Button pressed
        global running
        running = not running
    while (not button.value):    # Wait for button to be released
        time.sleep(0.1)


def lookAround():
    '''Main routine to look all around'''
    # Group 1
    servo1.angle = random.randint(ANGLE_MIN, ANGLE_MAX)
    servo2.angle = random.randint(ANGLE_MIN, ANGLE_MAX)
    servo3.angle = random.randint(ANGLE_MIN, ANGLE_MAX)
    servo4.angle = random.randint(ANGLE_MIN, ANGLE_MAX)

    flicker(dot)
    time.sleep(0.2)
    checkButton()

    flicker(dot)
    time.sleep(0.1)
    checkButton()

    flicker(dot)
    time.sleep(0.2)
    checkButton()

    # Group 2
    servo5.angle = random.randint(ANGLE_MIN, ANGLE_MAX)
    servo6.angle = random.randint(ANGLE_MIN, ANGLE_MAX)
    servo7.angle = random.randint(ANGLE_MIN, ANGLE_MAX)
    servo8.angle = random.randint(ANGLE_MIN, ANGLE_MAX)

    flicker(dot)
    time.sleep(0.2)
    checkButton()

    flicker(dot)
    time.sleep(0.1)
    checkButton()

    # Group 3
    servo9.angle = random.randint(ANGLE_MIN, ANGLE_MAX)
    servo10.angle = random.randint(ANGLE_MIN, ANGLE_MAX)
    servo11.angle = random.randint(ANGLE_MIN, ANGLE_MAX)
    # servo12 needs to be piggybacked on some other servo's pin - see above
    # servo12.angle = random.randint(ANGLE_MIN, ANGLE_MAX)

    flicker(dot)
    time.sleep(0.2)
    checkButton()

    flicker(dot)
    time.sleep(0.1)
    checkButton()

    flicker(dot)
    time.sleep(0.2)
    checkButton()

def stare():
    '''Reset servos to midpoint'''
    global staring
    if (not staring):
        servo1.angle = ANGLE_MIDPOINT
        servo2.angle = ANGLE_MIDPOINT
        servo3.angle = ANGLE_MIDPOINT
        servo4.angle = ANGLE_MIDPOINT
        servo5.angle = ANGLE_MIDPOINT
        servo6.angle = ANGLE_MIDPOINT
        servo7.angle = ANGLE_MIDPOINT
        servo8.angle = ANGLE_MIDPOINT
        servo9.angle = ANGLE_MIDPOINT
        servo10.angle = ANGLE_MIDPOINT
        servo11.angle = ANGLE_MIDPOINT
        # servo12 needs to be piggybacked on some other servo's pin - see above
        # servo12.angle = ANGLE_MIDPOINT
        staring = True


######################### MAIN LOOP ##############################

while True:
    checkButton()   # No interrupts in CircuitPython, so we have to poll
    if running:
        staring = False
        lookAround()
    else:
        stare()
