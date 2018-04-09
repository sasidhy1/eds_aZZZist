import os
import time

### OFF CHIME ###

d4 = 0.2  # second
f4 = 450  # Hz
d5 = 0.2  # second
f5 = 300  # Hz

os.system('play --no-show-progress --null --channels 1 synth %s sine %f' % (d4, f4))
os.system('play --no-show-progress --null --channels 1 synth %s sine %f' % (d5, f5))