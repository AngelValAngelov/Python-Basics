import math

snowball = int(input())

snowball_value = 0
best_value = 0
best_snow = 0
best_time = 0
best_quality = 0

for snowball in range(snowball):
    snowball_snow = int(input())
    snowball_time = int(input())
    snowball_quality = int(input())
    snowball_value = (snowball_snow // snowball_time)
    snowball_result = math.pow(snowball_value,snowball_quality)

    if snowball_result > best_value:
        best_value = snowball_result
        best_snow = snowball_snow
        best_time = snowball_time
        best_quality = snowball_quality
print(f"{best_snow} : {best_time} = {int(best_value)} ({best_quality})")