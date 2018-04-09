import os
import time
from random import *
import sys
import pygame

start_time = time.time()
t_end1 = start_time + 60 * 5
t_end2 = t_end1 + 60 * 15

pygame.mixer.init()
pygame.mixer.music.load("/home/pi/Desktop/eds_azzzist/SAMPLES/kat_beep.wav")
pygame.mixer.music.play()

while time.time() <= t_end1:

	rand1 = uniform(5, 10)

	pygame.mixer.music.play()
	print("---------------------------------------------")
	print("waiting..........")

	print("random interval: {}").format(rand1)
	time.sleep(rand1)

print("----------------------------------------------------------")
print("running for 5 minutes, random between 1 and 2 minutes")
t_end = time.time() + 60 * 7

while (time.time() <= t_end2) and (time.time() > t_end1):

	rand2 = uniform(60, 120)

	pygame.mixer.music.play()
	print("---------------------------------------------")
	print("waiting..........")

	print("random interval: {}").format(rand2)
	time.sleep(rand2)

print("----------------------------------------------------------")
print(time.time())
