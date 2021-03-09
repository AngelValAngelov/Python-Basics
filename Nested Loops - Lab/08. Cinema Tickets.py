movie_name = input()
student = 0
standard = 0
kid = 0
all_people = 0
while movie_name != "Finish":
    free_places = int(input())
    booked_places = 0
    ticket_type = input()
    while ticket_type != "End":
        all_people += 1
        booked_places += 1
        if ticket_type == "student":
            student += 1
        elif ticket_type == "standard":
            standard += 1
        elif ticket_type == "kid":
            kid += 1
        if booked_places == free_places:
            break
        ticket_type = input()

    percent = (booked_places / free_places) * 100
    print(f"{movie_name} - {percent:.2f}% full.")
    movie_name = input()

percent_students = (student / all_people) * 100
percent_standard = (standard / all_people) * 100
percent_kid = (kid / all_people) * 100

print(f"Total tickets: {all_people}")
print(f"{percent_students:.2f}% student tickets.")
print(f"{percent_standard:.2f}% standard tickets.")
print(f"{percent_kid:.2f}% kids tickets.")