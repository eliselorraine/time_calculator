import re

def add_time(start, duration, day=None):

    start_hr = int(start.split(':')[0])
    start_min = int(start.split(':')[1].split(' ')[0])
    time_of_day = start.split(' ')[1]
    next_day = False
    new_day = day

    duration_hr = int(duration.split(':')[0])
    duration_min = int(duration.split(':')[1])

    if day is not None and duration_hr >= 24 :
        print(day)
        days_of_week = ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday')
        # look up what day it is in the dictionary. remember case insensitivity
        
        for d in days_of_week :
            d = d.lower()
            param_day = day.lower()
            index = d.find(param_day)
            print(index)
        # use the lookup to grab the index of the day it is
        # add that index to the days passed. 

        day_n = int(duration_hr / 24)
        while day_n > 7 :
            day_n -= 7
        new_day = days_of_week[day_n]
        print(new_day)

    new_time_hr = start_hr + duration_hr
    new_time_min = start_min + duration_min

    if new_time_min >= 60 :
        new_time_min -= 60
        new_time_hr += 1

    if duration_hr >= 24:
        n = int(duration_hr / 24) + 1
        if duration_hr == 24 and duration_min == 0:
            n = 1
        while new_time_hr >= 12 :
            if time_of_day == 'AM':
                time_of_day = 'PM'
            else :
                time_of_day = 'AM'
            if new_time_hr == 12 :
                break
            new_time_hr -= 12
        if new_time_min < 10:
            new_time_min = f"0{new_time_min}"
        if n > 1 :
            return f"{new_time_hr}:{new_time_min} {time_of_day} ({n} days later)"
        return f"{new_time_hr}:{new_time_min} {time_of_day} (next day)"


    if new_time_hr == 12 and time_of_day == "PM":
        next_day = True
        time_of_day = "AM"
    elif new_time_hr > 12 and time_of_day == "PM":
        new_time_hr -= 12
        next_day = True
        time_of_day = "AM"
    elif new_time_hr == 12:
        time_of_day = "PM"
    elif new_time_hr > 12 :
        new_time_hr -= 12
        time_of_day = "PM"
    
    str_new_time_min = str(new_time_min)
    
    if len(str_new_time_min) == 1:
        str_new_time_min = "0" + str_new_time_min

    if day is not None and next_day != True :
        new_time = f"{new_time_hr}:{str_new_time_min} {time_of_day}, {new_day}"
    elif day is None and next_day :
        new_time = f"{new_time_hr}:{str_new_time_min} {time_of_day} (next day)"
    else :
        new_time = f"{new_time_hr}:{str_new_time_min} {time_of_day}"
    
    return new_time

    

