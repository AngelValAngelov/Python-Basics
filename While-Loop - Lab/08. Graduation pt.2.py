name = input()
year_mark = float(input())
years = 1
result = 0
count_bad_marks = 0

while years <= 12:
    if year_mark >= 4.00:
        years += 1
        result = result + year_mark
        if years == 13:
            print(f"{name} graduated. Average grade: {result / 12:.2f}")
            break
        else:
            year_mark = float(input())
            count_bad_marks = 0
    else:
        if count_bad_marks < 1:
            count_bad_marks += 1
            year_mark = float(input())
        else:
            print(f"{name} has been excluded at {years} grade")
            break

