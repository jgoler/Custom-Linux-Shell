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
        # Here is the updated solution from lines 36-43
        num_jobs = len(jobs)
        x = 0
        process_existence = False
        while x < num_jobs:
            if process_id in jobs[x]:
                process_existence = True
            x += 1
        if not process_existence:
            print("You entered a process id that doesn't exist")
        else:
            os.kill(int(process_id), signal.SIGSTOP)
            os.kill(int(process_id), signal.SIGCONT)    
    elif command[0:2] == "fg":
        process_id = command[3:]
        count = 0
        num_jobs = len(jobs)
        x = 0
        process_existence = False
        while x < num_jobs:
            if process_id in jobs[x]:
                process_existence = True
            x += 1
        if not process_existence:
            print("You entered a process id that doesn't exist")
        else:
            os.kill(int(process_id), signal.SIGSTOP)
            for y in command_list:
                if y[1] == process_id:
                    count = y[0] 
            count.wait()
    else:                                                                       
        args = shlex.split(command)
        count = subprocess.Popen(args)
        #append process name, and process id 
        jobs.append(command + " | " + str(count.pid))
        command_list.append((count, count.pid))
    count += 1