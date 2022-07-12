import pytz
import datetime
from datetime import datetime
import time


while True:
    userinput = input("Enter input time zone:  ")
    timezones = pytz.all_timezones
    
    if userinput in timezones:
        file = open("input-timezone.txt", "w")
        file.write(userinput)
        file.close()
    else: 
        print("Must enter a valid time zone.")

    userinput = input("Enter output time zone:  ")
    timezones = pytz.all_timezones
    
    if userinput in timezones:
        file = open("output-timezone.txt", "w")
        file.write(userinput)
        file.close()
    else: 
        print("Must enter a valid time zone.")

    datetime = str(input('Enter date and time (yyyy-mm-dd hh:mm): '))
    
    file = open("datetime.txt", "w")    
    file.write(datetime)
    file.close()
    time.sleep(5.0) 

    file = open("output-time.txt", "r")
    output = file.read()
    file.close()

    file = open("output-timezone.txt", "r")
    outputzone = file.read()
    file.close()
    time.sleep(10.0)  

    print(f"Time in {outputzone}: {output}") 
 