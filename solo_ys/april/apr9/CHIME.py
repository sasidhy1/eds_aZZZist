import os
import time

### ON CHIME ###

d1 = 0.1  # second
f1 = 450  # Hz
d2 = 0.1  # second
f2 = 550  # Hz
d3 = 0.1  # second
f3 = 650  # Hz

os.system('play --no-show-progress --null --channels 1 synth %s sine %f' % (d1, f1))
os.system('play --no-show-progress --null --channels 1 synth %s sine %f' % (d2, f2))
os.system('play --no-show-progress --null --channels 1 synth %s sine %f' % (d3, f3))

time.sleep(1)

### OFF CHIME ###

d4 = 0.1  # second
f4 = 450  # Hz

os.system('play --no-show-progress --null --channels 1 synth %s sine %f' % (d4, f4))
os.system('play --no-show-progress --null --channels 1 synth %s sine %f' % (d4, f4))