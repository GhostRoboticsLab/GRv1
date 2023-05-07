#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""SPECIFICATION
Electronic specifications
Operating voltage: 4.8-7.2V
6V test environment
Operating speed (no load): 0.18 sec/60 degrees
Resting current: 80mA
Locking torque: 11.5KG*cm
Stall current: 1.4A
Standby current: 4mA
7V test environment
Operating speed (no load): 0.16sec/60 degrees
Resting current: 100mA
Locking torque: 12KG*cm
Stall current: 1.76A
Standby current: 5mA
Mechanical specifications
Gear material: metal gear
Operating angle: 270 degrees
Wiring gauge: 28PVC
Data line length: 320mm
Gear bracket spline: 25T/5.80
Gear ratio: 310:1
Size: 54.5*20*47.5mm
Control specifications
Feedback signal: 0-3.3V
Control signal: RC PWM
Pulse range: 500-2500 us
Median signal value: 1500us
Clockwise rotation: <1500us
Control frequency: 50-330Hz (Arduino compatible)
"""

#Libraries
import time     #https://docs.python.org/fr/3/library/time.html
from adafruit_servokit import ServoKit    #https://circuitpython.readthedocs.io/projects/servokit/en/latest/

#Constants
nbPCAServo=16

#Parameters
MIN_IMP  =[500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500]
MAX_IMP  =[2500, 2500, 2500, 2500, 2500, 2500, 2500, 2500, 2500, 2500, 2500, 2500, 2500, 2500, 2500, 2500]
MIN_ANG  =[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
MAX_ANG  =[270, 270, 270, 270, 270, 270, 270, 270, 270, 270, 270, 270, 270, 270, 270, 270]

#Objects
pca = ServoKit(channels=16)

# function init
def init():

    for i in range(nbPCAServo):
        pca.servo[i].set_pulse_width_range(MIN_IMP[i] , MAX_IMP[i])


# function main
def main():

    pcaScenario();


# function pcaScenario
def pcaScenario():
    """Scenario to test servo"""
    for i in range(nbPCAServo):
        for j in range(MIN_ANG[i],MAX_ANG[i],1):
            print("Send angle {} to Servo {}".format(j,i))
            pca.servo[i].angle = j
            time.sleep(0.01)
        for j in range(MAX_ANG[i],MIN_ANG[i],-1):
            print("Send angle {} to Servo {}".format(j,i))
            pca.servo[i].angle = j
            time.sleep(0.01)
        pca.servo[i].angle=None #disable channel
        time.sleep(0.5)




if __name__ == '__main__':
    init()
    main()