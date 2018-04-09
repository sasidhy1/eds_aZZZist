import os
import time
from random import *
import sys

start_time = time.time()
t_end1 = start_time + 60 * 5
t_end2 = t_end1 + 60 * 15

while time.time() <= t_end1:

	rand1 = uniform(5, 10)

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

	print("random interval: {}").format(rand1)
	time.sleep(rand1)

print("----------------------------------------------------------")
print("running for 5 minutes, random between 1 and 2 minutes")
t_end = time.time() + 60 * 7

while (time.time() <= t_end2) and (time.time() > t_end1):

	rand2 = uniform(60, 120)

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

	print("random interval: {}").format(rand2)
	time.sleep(rand2)

print("----------------------------------------------------------")
print(time.time())
