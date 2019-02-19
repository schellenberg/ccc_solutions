#j4 - arrival time (2016)

def is_rush_hour(hour):
    #assumes minute is 00
    return hour >= 7 and hour < 10 or hour >= 15 and hour < 19

def pretty_print_time(hour, minute):
    if hour < 10:
        hour = "0" + str(hour)
    if minute < 10:
        minute = "0" + str(minute)
    print(str(hour) + ":" + str(minute))

raw_time = input()
info = raw_time.split(":")
hour_left = int(info[0])
minute_left = int(info[1])

time_left = 120
current_hour = hour_left
current_minute = minute_left

# get to an exact hour
if current_minute != 0:
    amount_to_on_the_hour = 60 - current_minute
    if (is_rush_hour(current_hour)):
        #takes twice as long during rush hour
        amount_to_on_the_hour = amount_to_on_the_hour // 2 
        
    time_left -= amount_to_on_the_hour
    current_minute = 0
    current_hour = (current_hour + 1) % 24

while time_left > 0:
    if is_rush_hour(current_hour):
        if time_left > 30:
            current_hour = (current_hour + 1) % 24
            time_left -= 30
        else:
            current_minute = time_left * 2
            time_left = 0
    else:
        if time_left >= 60:
            current_hour = (current_hour + 1) % 24
            time_left -= 60
        else:
            current_minute = time_left
            time_left = 0

pretty_print_time(current_hour, current_minute)
    
