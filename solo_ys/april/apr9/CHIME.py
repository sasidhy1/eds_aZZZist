import os
import time

### ON CHIME ###

d1 = 0.1  # second
f1 = 300  # Hz
d2 = 0.1  # second
f2 = 380  # Hz
d3 = 0.1  # second
f3 = 450  # Hz

os.system('play --no-show-progress --null --channels 1 synth %s sine %f' % (d1, f1))
os.system('play --no-show-progress --null --channels 1 synth %s sine %f' % (d2, f2))
os.system('play --no-show-progress --null --channels 1 synth %s sine %f' % (d3, f3))

time.sleep(1)

### OFF CHIME ###

d4 = 0.2  # second
f4 = 450  # Hz
d5 = 0.2  # second
f5 = 300  # Hz
# d6 = 0.1  # second
# f6 = 250  # Hz


os.system('play --no-show-progress --null --channels 1 synth %s sine %f' % (d4, f4))
os.system('play --no-show-progress --null --channels 1 synth %s sine %f' % (d5, f5))
# os.system('play --no-show-progress --null --channels 1 synth %s sine %f' % (d6, f6))

# os.system('play --no-show-progress --null --channels 1 synth %s sine %f fade q .02 .05 .02' % (d4, f4))
# os.system('play --no-show-progress --null --channels 1 synth %s sine %f fade q .02 .05 .02' % (d4, f4))