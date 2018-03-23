import os
import time
from random import *

print("----------------------------------------------------------")
print("running for 3 minutes, random between 5 and 10 seconds")
t_end = time.time() + 60 * 3

while time.time() < t_end:

	rand = uniform(5, 10)

	duration = 0.5  # second
	freq = 450  # Hz
	print("beep 1")
	os.system('play --no-show-progress --null --channels 1 synth %s sine %f' % (duration, freq))
	time.sleep(0.5)
	print("beep 2")
	os.system('play --no-show-progress --null --channels 1 synth %s sine %f' % (duration, freq))
	time.sleep(0.5)
	print("beep 3")
	os.system('play --no-show-progress --null --channels 1 synth %s sine %f' % (duration, freq))
	time.sleep(0.5)
	print("---------------------------------------------")
	print("waiting..........")

	print("random interval: {}").format(rand)
	time.sleep(rand)

print("----------------------------------------------------------")
print("running for 5 minutes, random between 1 and 2 minutes")
t_end = time.time() + 60 * 7

while time.time() < t_end:

	rand = uniform(60, 120)

	duration = 0.5  # second
	freq = 450  # Hz
	print("beep 1")
	os.system('play --no-show-progress --null --channels 1 synth %s sine %f' % (duration, freq))
	time.sleep(0.5)
	print("beep 2")
	os.system('play --no-show-progress --null --channels 1 synth %s sine %f' % (duration, freq))
	time.sleep(0.5)
	print("beep 3")
	os.system('play --no-show-progress --null --channels 1 synth %s sine %f' % (duration, freq))
	time.sleep(0.5)
	print("---------------------------------------------")
	print("waiting..........")

	print("random interval: {}").format(rand)
	time.sleep(rand)