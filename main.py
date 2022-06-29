from time_calculator import add_time

print(add_time("11:06 PM", "2:02")) # 1:08 AM (next day)
print(add_time("3:30 PM", "2:12")) # "5:42 PM"
print(add_time("11:55 AM", "3:12")) # "3:07 PM"
print(add_time("9:15 PM", "5:30")) # "2:45 AM (next day)"
print(add_time("9:15 PM", "5:30")) # "2:45 AM (next day)"
print(add_time("11:40 AM", "0:25")) # "12:05 PM"
print(add_time("2:59 AM", "24:00")) # "2:59 AM (next day)"
print(add_time("11:59 PM", "24:05")) # "12:04 AM (2 days later)"
