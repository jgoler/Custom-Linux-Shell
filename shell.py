import os
import time 
import subprocess
import shlex
import signal 
count = 0 
isTerminated = False
while not isTerminated:
    if count == 0:
        jobs = ["Process | ID"]
    location = os.getcwd()
    time1 = time.localtime()
    actual_time = str(time.strftime("%c", time1))
    promptText = location + " " + actual_time + " ~ $ "
    command = input(promptText)
    if command == "exit":
        isTerminated = True
    elif command == "cd ..":
        os.chdir('..')
    elif command[0:2] == "cd":   
        os.chdir(command[3:])
    elif command == "jobs":
        for x in jobs:
            print(x, '\n') 
    elif command == "ls":
        os.system("ls")
    elif command == "pwd":
        os.system("pwd")
    elif command[0:2] == "bg":
        process_id = command[3:]                            
        #want to check if it truly is an existing process
        for x in jobs:
            #does process_id exist in x
            if process_id not in x:
                print("You entered a process id that doesn't exist")
        q = subprocess.Popen(process_id, signal.SIGCONT)
    else:    
        args = shlex.split(command)
        p = subprocess.Popen(args)
        #append process name, and process id 
        jobs.append(command + " | " + str(p.pid))
    count += 1