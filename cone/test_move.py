# import the necessary packages
from picamera.array import PiRGBArray
import picamera
import time
import cv2
import numpy as np
import PicoBorgRev
import math
import sys
import Move

# Setup the PicoBorg Reverse
PBR = PicoBorgRev.PicoBorgRev()
#PBR.i2cAddress = 0x44                  # Uncomment and change the value if you have changed the board address
PBR.Init()
#PBR.SetEpoIgnore(True)                 # Uncomment to disable EPO latch, needed if you do not have a switch / jumper
PBR.SetCommsFailsafe(False)             # Disable the communications failsafe
PBR.ResetEpo()
 
# Movement settings (worked out from our DiddyBorg on a smooth surface)
timeForward1m = 5.7                     # Number of seconds needed to move about 1 meter
timeSpin360   = 4.8                     # Number of seconds needed to make a full left / right spin
testMode = False                        # True to run the motion tests, False to run the normal sequence
 
# Power settings
voltageIn = 12.0                        # Total battery voltage to the PicoBorg Reverse
voltageOut = 6.0                        # Maximum motor voltage
 
# Setup the power limits
if voltageOut > voltageIn:
    maxPower = 1.0
else:
    maxPower = voltageOut / float(voltageIn)
 
# Function to perform a general movement
def PerformMove(driveLeft, driveRight, numSeconds):
    # Set the motors running
    PBR.SetMotor1(driveRight * maxPower)
    PBR.SetMotor2(-driveLeft * maxPower)
    # Wait for the time
    time.sleep(numSeconds)
    # Turn the motors off
    PBR.MotorsOff()
 
# Function to spin an angle in degrees
def PerformTurn(angle, speed):
    PBR.MotorsOff()
    if angle < 0.0:
        # Left turn
        driveLeft  = -1.0
        driveRight = +1.0
        angle *= -1
    else:
        # Right turn
        driveLeft  = +1.0
        driveRight = -1.0
    # Calculate the required time delay
    numSeconds = (angle / 360.0) * timeSpin360
    # Perform the motion
    PerformMove(driveLeft, driveRight, numSeconds)

#def PerformSpin(angle, speed):
#    PBR.MotorsOff()
#    if angle < 0.0:
#        # Left turn
#        driveLeft  = -1.0
#        driveRight = +1.0
#        angle *= -1
#    else:
#        # Right turn
#        driveLeft  = +1.0
#        driveRight = -1.0
#    # Calculate the required time delay
#    numSeconds = (angle / 360.0) * timeSpin360
#    # Perform the motion
#    PerformMove(driveLeft*speed, driveRight*speed, numSeconds)


# 
# Function to drive a distance in meters
def PerformDrive(meters):
    if meters < 0.0:
        # Reverse drive
        driveLeft  = -1.0
        driveRight = -1.0
        meters *= -1
    else:
        # Forward drive
        driveLeft  = +1.0
        driveRight = +1.0
    # Calculate the required time delay
    numSeconds = meters * timeForward1m
    # Perform the motion
    PerformMove(driveLeft, driveRight, numSeconds)


speed = 0.5	
i = 0
while i < 5:
	PBR.MotorsOff()
	time.sleep(5)
	Move.bypass(PBR)
	i += 1

PBR.MotorsOff()
