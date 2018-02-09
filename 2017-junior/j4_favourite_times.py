# favourite times

def add_minute(time):
    separator = time.find(':')
    hour = int(time[:separator])
    minute = int(time[separator+1:])
    if minute == 59:
        hour = (hour + 1) % 12
        if hour == 0:
            hour = 12
        minute = 0
    else:
        minute += 1
    if minute < 10:
        str_minute = "0" + str(minute)
    else:
        str_minute = str(minute)
    new_time = str(hour) + ":" + str_minute
    return new_time

def arithmetic_sequence_check(time):
    number_list = []
    for location, value in enumerate(time):
        if value != ":":
            number_list.append(int(time[location]))
    difference = number_list[1] - number_list[0]
    for counter in range(1, len(time)-1):
        if (number_list[counter] - number_list[counter-1]) != difference:
            return False
    return True

duration = int(input())
time = "12:00"

first_part = 0
if duration >= 720:  #12*60
    multiplier = duration // 720
    twelve_hour_count = 0
    for counter in range(720):
        time = add_minute(time)
        if arithmetic_sequence_check(time):
            twelve_hour_count += 1
    first_part = twelve_hour_count * multiplier


time = "12:00"
modded_duration = duration % 720

second_part = 0
for counter in range(modded_duration):
    time = add_minute(time)
    if arithmetic_sequence_check(time):
        second_part += 1
    
total = first_part + second_part
print(total)

