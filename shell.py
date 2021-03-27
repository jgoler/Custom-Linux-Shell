
import os
import time 
import subprocess
import shlex
import signal 
import copy
count = 0 
command_list = []
isTerminated = False
foreground_id = 0
while not isTerminated:
    if foreground_id != 0:
        for x in command_list:
            if x[1] == foreground_id:
                #if it is no longer running then we want make foreground_id 0   
                if x[0].poll() != None:
                    foreground_id = 0
    try:
        if count == 0:
            jobs = ["Process | ID"]
        found_process = False
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
        elif command.find('|')!= -1:
            command_list = []
            num_commands = command.count('|')
            num = 0
            while (num < num_commands):
                try:
                    pipe_pos = command.index('|')
                    search_pos = int(pipe_pos) - 1
                    current_command = command[0:search_pos]
                    command_list.append(current_command)
                    command = command[pipe_pos + 2:]
                    num += 1
                except:
                    num += 1
            command_list.append(command[0:])
            print(command_list)
        elif command[0:2] == "fg":
            process_id = command[3:]
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
                y = 0
                while y < len(command_list):
                    if command_list[y][1] == process_id:
                        foreground_id = copy.copy(process_id)
                        command_list[y][0].wait()
        else:   
            try:                                                                    
                args = shlex.split(command)
                command_list.append([3,5])
                index = len(command_list) - 1
                command_list[index][0] = subprocess.Popen(args)
                proc_id = command_list[index][0].pid
                command_list[index][1] = proc_id
                #append process name, and process id    
                jobs.append(command + " | " + str(proc_id))
            except:
                print("invalid command")
        count += 1
    except KeyboardInterrupt:
        #find process id of current foreground job if there is one
        #send that process a SIGINT signal  
        #if foreground id is not currently running, then print "no current process in foreground"
        if foreground_id == 0:
            print("No current process in the foreground")
        else:
            os.kill(foreground_id, signal.SIGINT)


