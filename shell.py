import os
import time 
import subprocess
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

    if command == "jobs":
    	ps = subprocess.Popen(['ps', 'aux'], stdout=subprocess.PIPE).communicate()[0]
    	print(ps)
    	processes = ps.split('\n')
    elif command[0:2] == "cd":   
        os.chdir(command[3:])

        location = os.getcwd()
    if command[0:1] == "cd":
        os.chdir(command[3:])
        location = os.getcwd()
    else:
        os.system(command)