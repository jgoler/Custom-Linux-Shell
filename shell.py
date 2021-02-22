import os 
from datetime import date 
isTerminated = False 


while not isTerminated: 	
	location = os.getcwd() 
	promptText = location + " " + str(date.today()) + " ~ $ " 
    command = input(promptText) 
    os.system(command)