#A function accepts the time in seconds and returns
#the time in hours

def time_in_seconds(seconds):
    hours = seconds/3600
    return hours
time_seconds = 72
time_hours = time_in_seconds(time_seconds)
print(time_hours)
    
