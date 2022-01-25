import time
import utime
import pycom
import machine
from machine import Pin

# initialise Ultrasonic Sensor pins
echo = Pin("P11", mode=Pin.IN) # Lopy4 specific: Pin('P20', mode=Pin.IN)
trigger = Pin("P12", mode=Pin.OUT) # Lopy4 specific Pin('P21', mode=Pin.IN)
trigger(0)

# Ultrasonic distance measurment
def distance_measure():
    # trigger pulse LOW for 2us (just in case)
    trigger.value(0)
    utime.sleep_us(5)
    # trigger HIGH for a 10us pulse
    trigger.value(1)
    utime.sleep_us(10)
    trigger.value(0)

    # wait for the rising edge of the echo then start timer
    start_time = int(time.time())
    while echo.value() == 0:
        if int(time.time()) - start_time > 3:
            print("Error1")
            raise Exception() 
        pass
    start = utime.ticks_us()

    # wait for end of echo pulse then stop timer
    start_time = int(time.time())
    while echo.value() == 1:
        if int(time.time()) - start_time > 3:
            print("Error2")
            raise Exception() 
        pass
    finish = utime.ticks_us()

    # pause for 20ms to prevent overlapping echos
    utime.sleep_ms(20)

    # calculate distance by using time difference between start and stop
    # speed of sound 340m/s or .034cm/us. Time * .034cm/us = Distance sound travelled there and back
    # divide by two for distance to object detected.
    distance = ((utime.ticks_diff(finish, start)) * .034)/2

    return distance