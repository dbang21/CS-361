import pytz
import datetime
from datetime import datetime

while True:

    file = open("input-timezone.txt", "r")  
    inputtimezone = file.readline()
    file.close()

    if inputtimezone:
        inputtimezone = pytz.timezone(inputtimezone)

    file = open("output-timezone.txt", "r")  
    outputtimezone = file.readline()
    file.close()

    if outputtimezone:
        outputtimezone = pytz.timezone(outputtimezone)

    file = open("datetime.txt", "r")  
    inputtime = file.readline()
    file.close()

    if inputtime:
        datetime = datetime.strptime(inputtime, "%Y-%m-%d %H:%M")
        inputtime = inputtimezone.localize(datetime) 
        outputtime = inputtime.astimezone(outputtimezone)
        file = open("output-time.txt", "w")
        file.write(str(outputtime))
        file.close()
    
