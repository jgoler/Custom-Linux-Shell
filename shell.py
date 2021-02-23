import os
import time 
isTerminated = False
while not isTerminated:
    location = os.getcwd()
    time1 = time.localtime()
    actual_time = str(time.strftime("%c", time1))
    promptText = location + " " + actual_time + " ~ $ "
    command = input(promptText)
    if command == "exit":
        isTerminated = True
    if command == "cd ..":
        os.chdir('..')
        location = os.getcwd()
    if command[0:1] == "cd":
        os.chdir(command[3:])
        location = os.getcwd()
    else:
        os.system(command)