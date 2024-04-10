import datetime
import time
import os
import random
import playsound
import schedule

print("Carillon TEST Program Open!")

# get the current date and time
now = datetime.datetime.now()

# define the path to your mp3 files and directory
mp3_file_single = "tolls/Single Chime Mastered.WAV"

# check for user input to play a specific mp3 file
command = input("Enter a command (type test to test): ")
if command.startswith("test"):
    print("Testing Begin")
    playsound.playsound(mp3_file_single)
    print("Testing End")
