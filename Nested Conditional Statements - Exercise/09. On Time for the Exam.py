hours = int(input())
minutes = int(input())
hour_come = int(input())
minutes_come = int(input())

time = ""
time_hour = 0
time_minutes = 0
all_time_exam = (hours * 60) + minutes
all_time_come = (hour_come * 60) + minutes_come
result = all_time_exam - all_time_come

if result < 0:
    time = "Late"
elif 30 < result:
    time = "Early"
else:
    time = "On time"

if 0 < result < 60:
    time_hours = 0
    time_minutes = result
    print(f"{time}\n{time_minutes} minutes before the start")
elif result >= 60:
    time_hour = result // 60
    time_minutes = result % 60
    print(f"{time}\n{time_hour}:{time_minutes:02d} hours before the start")
elif -60 < result < 0:
    time_hour = 0
    time_minutes = abs(result)
    print(f"{time}\n{time_minutes} minutes after the start")
elif result == 0:
    print(f"{time}")
else:
    time_hour = abs(result) // 60
    time_minutes = abs(result) % 60
    print(f"{time}\n{time_hour}:{time_minutes:02d} hours after the start")
