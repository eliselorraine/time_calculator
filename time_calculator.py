def add_time(start, duration, day=None):
    # add duration time to start time and return the result
    # if result is the next day, it should show "next day" after the time
    # if the result is more than one day later, it should show "n days later" after the time

    # maybe we could convert to military time and then go back? 

    start_hr = int(start.split(':')[0])
    start_min = int(start.split(':')[1].split(' ')[0])
    time_of_day = start.split(' ')[1]
    next_day = False

    duration_hr = int(duration.split(':')[0])
    duration_min = int(duration.split(':')[1])

    new_time_hr = start_hr + duration_hr
    new_time_min = start_min + duration_min

    if new_time_min >= 60 :
        new_time_min -= 60
        new_time_hr += 1

    if duration_hr >= 24:
        n = -1
        while new_time_hr >= 12 :
            if time_of_day == 'AM':
                time_of_day = 'PM'
                n += 1
            else :
                n += 1
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

    if next_day :
        new_time = f"{new_time_hr}:{str_new_time_min} {time_of_day} (next day)"
    else :
        new_time = f"{new_time_hr}:{str_new_time_min} {time_of_day}"
    
    return new_time

    

