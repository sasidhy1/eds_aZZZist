import os
import time
from random import *
import sys
import matplotlib.pyplot as plt
import numpy as np
import wave

wavef = wave.open('beep.wav','w')

sampleRate = 44100.0 # hertz
duration = 0.5  # second
freq = 450  # Hz

ack = os.system('play --no-show-progress --null --channels 1 synth %s sine %f' % (duration, freq))
kd = os.system('play --no-show-progress --null --channels 1 synth 0.5 sine 0'

Wave_write.writeframes(ack)
Wave_write.writeframes(kd)
Wave_write.writeframes(ack)
Wave_write.writeframes(kd)
Wave_write.writeframes(ack)
Wave_write.writeframes(kd)