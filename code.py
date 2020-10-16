# Itsy Bitsy M0 Express IO demo
# Welcome to CircuitPython 4 :)

import board
import time
import gc
import random
from digitalio import DigitalInOut, Direction, Pull
import pulseio
import adafruit_dotstar
from adafruit_motor import servo

# One pixel connected internally!
dot = adafruit_dotstar.DotStar(board.APA102_SCK, board.APA102_MOSI, 1, brightness=0.5)

# Built in red LED
# led = DigitalInOut(board.D13)
# led.direction = Direction.OUTPUT

# PWM available on the following, though not all at once!
# From https://learn.adafruit.com/introducing-itsy-bitsy-m0/circuitpython-pwm:
# No PWM on: A0
# No PWM on: A1
# PWM on: A2
# PWM on: A3
# PWM on: A4
# No PWM on: A5
# PWM on: APA102_MOSI
# PWM on: APA102_SCK
# PWM on: D0
# PWM on: D1
# PWM on: D10
# PWM on: D11
# PWM on: D12
# PWM on: D13
# PWM on: D2
# PWM on: D3
# PWM on: D4
# PWM on: D5
# PWM on: D6
# PWM on: D7
# PWM on: D8
# PWM on: D9
# PWM on: L
# PWM on: MISO
# PWM on: MOSI
# PWM on: RX
# PWM on: SCK
# PWM on: SCL
# PWM on: SDA
# PWM on: TX



servo1 = servo.Servo(pulseio.PWMOut(board.D10, frequency=50))
servo2 = servo.Servo(pulseio.PWMOut(board.D1, frequency=50))
servo3 = servo.Servo(pulseio.PWMOut(board.D2, frequency=50))
servo4 = servo.Servo(pulseio.PWMOut(board.D3, frequency=50))
servo5 = servo.Servo(pulseio.PWMOut(board.D5, frequency=50))
servo6 = servo.Servo(pulseio.PWMOut(board.D7, frequency=50))
servo7 = servo.Servo(pulseio.PWMOut(board.D9, frequency=50))
servo8 = servo.Servo(pulseio.PWMOut(board.D11, frequency=50))
servo9 = servo.Servo(pulseio.PWMOut(board.D13, frequency=50))
servo10 = servo.Servo(pulseio.PWMOut(board.SCK, frequency=50))
servo11 = servo.Servo(pulseio.PWMOut(board.SCL, frequency=50))
# Can't figure out how to get a 12th PWM, so piggyback servo 12 on some other servo's pin
# servo12 = servo.Servo(pulseio.PWMOut(board.A2, frequency=50))


######################### HELPERS ##############################

def flicker():
    '''Generate a random color in the orange-ish spectrum, like a flame'''
    r = random.randint(50, 200)
    g = random.randint(0, 80)   # If changing this, beware of overflow on the next line
    r = r if r > g else g + 20
    b = 0
    return [r, g, b]


######################### MAIN LOOP ##############################

while True:
  dot[0] = flicker()

#   servo1.angle = random.randint(0, 180)
#   servo2.angle = random.randint(0, 180)
#   servo3.angle = random.randint(0, 180)
#   servo4.angle = random.randint(0, 180)
  time.sleep(0.2)
  dot[0] = flicker()
  time.sleep(0.1)
  dot[0] = flicker()
  time.sleep(0.2)

#   servo5.angle = random.randint(0, 180)
#   servo6.angle = random.randint(0, 180)
#   servo7.angle = random.randint(0, 180)
#   servo8.angle = random.randint(0, 180)
  time.sleep(0.2)
  dot[0] = flicker()
  time.sleep(0.1)
  dot[0] = flicker()

#   servo9.angle = random.randint(0, 180)
#   servo10.angle = random.randint(0, 180)
#   servo11.angle = random.randint(0, 180)
# #   servo12.angle = random.randint(0, 180)
  time.sleep(0.2)
  dot[0] = flicker()
  time.sleep(0.1)
  dot[0] = flicker()
  time.sleep(0.2)
