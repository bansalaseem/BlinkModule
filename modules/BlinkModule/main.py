# Copyright (c) Microsoft. All rights reserved.
# Licensed under the MIT license. See LICENSE file in the project root for
# full license information.

import random
import time
import sys


# Choose HTTP, AMQP or MQTT as transport protocol.  Currently only MQTT is supported. test

def main(protocol):
    import RPi.GPIO as GPIO
    from time import sleep
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(18, GPIO.OUT)
    while True:
        GPIO.output(18, GPIO.HIGH)
        sleep(1)
        GPIO.output(18, GPIO.LOW)
        sleep(1)
    """from time import sleep
    led = LED(17)
    while True:
        led.on()
        sleep(1)
        led.off()
        sleep(1)"""
    print ( "\nPython %s\n" % sys.version )
    print ( "IoT Hub Client for Python" )

    while True:
        time.sleep(1)

if __name__ == '__main__':
    main("abc")
