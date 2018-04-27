# import necessary packages
import os
import time
from random import *
import sys

# initialize variables
duration = 0.5	# seconds
freq = 450		# Hz

# create writeable data files
out1 = open('output1.txt', 'w')
out2 = open('output2.txt', 'w')

# initialize start time, total runtime = 20 minutes
start_time = time.time()
t_end1 = start_time + 60 * 5	# runtime1 = 5 minutes 
t_end2 = t_end1 + 60 * 15		# runtime2 = 15 minutes

print("----------------------------------------------------------")
print("running for 5 minutes, random between 5 and 10 seconds")
print("----------------------------------------------------------")

# emits 3 beeps at specified freq; 0.5s on, 0.5s off
while time.time() <= t_end1:

	rand1 = uniform(5, 10)		# generate random intervals between 5-10 seconds
	for i in range(0,3):
		print "beep", i+1	
		os.system('play --no-show-progress --null --channels 1 synth %s sine %f' % (duration, freq))
		time.sleep(0.5)

	# append to data file
	out1 = open('output1.txt', 'a')
	out1.write(str(rand1))
	out1.write("\n")

	print("---------------------------------------------")
	print("waiting..........")

	print("random interval: {}").format(rand1)	# print generated random interval
	time.sleep(rand1)

print("----------------------------------------------------------")
print("running for 15 minutes, random between 1 and 2 minutes")
print("----------------------------------------------------------")

# emits 3 beeps at specified freq; 0.5s on, 0.5s off
while (time.time() <= t_end2) and (time.time() > t_end1):

	rand2 = uniform(60, 120)	# generate random intervals between 1-2 minutes
	for i in range(0,3):
		print "beep", i+1	
		os.system('play --no-show-progress --null --channels 1 synth %s sine %f' % (duration, freq))
		time.sleep(0.5)

	# append to data file
	out2 = open('output2.txt', 'a')
	out2.write(str(rand2))
	out2.write("\n")

	print("---------------------------------------------")
	print("waiting..........")

	print("random interval: {}").format(rand2)	# print generated random interval
	time.sleep(rand2)

print("----------------------------------------------------------")
print(time.time())				# print end time
