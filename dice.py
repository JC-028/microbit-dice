from microbit import*
import random, time
while True:
	if accelerometer.was_gesture('shake'):
		display.show(str(random.randint(1,6)))
		time.sleep(1)
