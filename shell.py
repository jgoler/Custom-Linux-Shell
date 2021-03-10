import os
import time 
import subprocess
import shlex
import signal 
count = 0 
command_list = []
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
        command_of_process = ""                      
        #want to check if it truly is an existing process
        for x in jobs:
            #does process_id exist in x
            if process_id not in x:
                print("You entered a process id that doesn't exist")
        os.kill(process_id, signal.SIGCONT)
        for y in command_list:
            if y[1] == process_id:
                command_of_process = y[0] 
        args = shlex.split(command_of_process)
        q = subprocess.Popen(args)
    elif command[0:2] == "fg":
        process_id = command[3:]
        command_of_process = ""
        for x in jobs:
            #does process_id exist in x
            if process_id not in x:
                print("You entered a process id that doesn't exist")
        os.kill(process_id, signal.SIGCONT)
        for y in command_list:
            if y[1] == process_id:
                command_of_process = y[0] 
        args = shlex.split(command_of_process)
        subprocess.run(args)
    else:                                                                       
        args = shlex.split(command)
        p = subprocess.Popen(args)
        #append process name, and process id 
        jobs.append(command + " | " + str(p.pid))
        command_list.append((command, p.pid))
    count += 1