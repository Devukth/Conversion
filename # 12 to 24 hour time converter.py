# 12 to 24 hour time converter
def convert_to_24(time):
    
    if (time[-2:] == "AM" and time[:2] == "12"):
        return "00" + time[2:-2]
        
    elif (time[-2:] == "AM"):
        return time[:-2]
    
    elif (time[-2:] == "PM" and time[:2] == "12"):
        return time[:-2]

    else:
        return str(int(time[:2]) + 12) + time[2:-2]

print(convert_to_24("12:39:59 AM"))