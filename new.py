command =""
started = False
stopped = True
while command  != "quit":
    command = input(">").lower()
    if command == "start" :
    	if started:
    		print("Car is already started")
    	else:
    	    started = True
    	    stopped = False	
    	    print("Car Started...")
    elif command == "stop" :
    	if stopped:
    		print("Car is already stopped")
    	else :
    	    stopped = True
    	    started = False
    	    print("Car stopped.")
    elif command == "help" :
    	print("""
start - to start the car
stop  - to stop the car
quit  - to quit
              """)
    elif command == "quit" :
        break	
    else :
        print("sorry i dont understand it...")	
            	