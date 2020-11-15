#!/usr/bin/env python

import RPi.GPIO as GPIO
from time import sleep

# The LEDs are wired to relay channel 3,
# which is controlled via GPIO 21.
# On the Raspberry Pi 4 this is physical pin 40.
relay = 21

def setup():
	GPIO.setmode(GPIO.BCM)
	GPIO.setup(relay, GPIO.OUT)

def set_lights_active(active=True):
	# The relays are active low,
	# so False turns them on
	# and True turns them off.
	GPIO.output(relay, not active)

if __name__ == "__main__":
	setup()
	while True:
		set_lights_active()
		sleep(3)
		set_lights_active(False)
		sleep(3)
	GPIO.cleanup()
