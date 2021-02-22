import os
import time 
isTerminated = False
while not isTerminated:
    location = os.getcwd()
    time1 = time.localtime()
    actual_time = str(time.strftime("%c", time1))
    promptText = location + " " + actual_time + " ~ $ "
    command = input(promptText)
    os.system(command)
    if command == exit:
        isTerminated = True 
    else:
        os.system(command)