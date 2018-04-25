import os
from random import *
import sys

duration = 0.5  # second
freq = 450  # Hz

print("user why u sleppin")
os.system('play --no-show-progress --null --channels 1 synth %s sine %f' % (duration, freq))