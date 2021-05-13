bad_marks = int(input())
name = input()
last_name = ""
mark = int(input())
mark_problems = 0
mark_count = 0
bad_marks_count = 0

while name != "Enough" or bad_marks != "Enough":
    if mark > 4:
        mark_problems += 1
        mark_count += mark
        last_name = name
        name = input()
        if name == "Enough":
            break
        else:
            mark = int(input())
    else:
        mark_count += mark
        bad_marks_count += 1
        mark_problems += 1
        if bad_marks_count >= bad_marks:
            print(f"You need a break, {bad_marks_count} poor grades.")
            break
        else:
            name = input()
            if name == "Enough":
                break
            else:
                mark = int(input())
if bad_marks_count < bad_marks:
    print(f"Average score: {mark_count / mark_problems:.2f}\nNumber of problems: {mark_problems}\nLast problem: {last_name}")
