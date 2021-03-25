from random import random # Generates random numbers
import math

print(random())

num_float = 23.6

print("Actual float value: " + str(num_float))
print(math.ceil(num_float))     #Round up
print(math.floor(num_float))    # Round down

import os, platform
import datetime, sys

working_directory = os.getcwd() #Tells us current directory
print(working_directory)
print(platform.uname())
print(os.cpu_count())
print(datetime.date.today())
print(sys.path)
print(math.pi)
