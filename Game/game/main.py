#titlescreen animation
from genderSelection import *
from animation import animate
import time


for x in range(0,7):
    animate(f"titlescreen/loading/{x}.txt")

anyKey = input("Press any key to continue...")

genderSelect()