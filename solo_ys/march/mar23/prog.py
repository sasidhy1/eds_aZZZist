import os
import time
from random import *
import sys

out1 = open('output1.txt', 'w')
out2 = open('output2.txt', 'w')

start_time = time.time()
t_end1 = start_time + 60 * 5
t_end2 = t_end1 + 60 * 15

while time.time() <= t_end1:

	rand1 = uniform(5, 10)

	duration = 0.5  # second
	freq = 450  # Hz
	os.system('play --no-show-progress --null --channels 1 synth %s sine %f' % (duration, freq))
	time.sleep(0.5)
	os.system('play --no-show-progress --null --channels 1 synth %s sine %f' % (duration, freq))
	time.sleep(0.5)
	os.system('play --no-show-progress --null --channels 1 synth %s sine %f' % (duration, freq))
	time.sleep(0.5)

	out1 = open('output1.txt', 'a')
	out1.write(str(rand1))
	out1.write("\n")
	time.sleep(rand1)

while (time.time() <= t_end2) and (time.time() > t_end1):

	rand2 = uniform(60, 120)

	duration = 0.5  # second
	freq = 450  # Hz
	os.system('play --no-show-progress --null --channels 1 synth %s sine %f' % (duration, freq))
	time.sleep(0.5)
	os.system('play --no-show-progress --null --channels 1 synth %s sine %f' % (duration, freq))
	time.sleep(0.5)
	os.system('play --no-show-progress --null --channels 1 synth %s sine %f' % (duration, freq))
	time.sleep(0.5)

	out2 = open('output2.txt', 'a')
	out2.write(str(rand2))
	out2.write("\n")
	time.sleep(rand2)