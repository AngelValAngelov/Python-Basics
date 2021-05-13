book_name = input()
books_count = int(input())
current_book = input()
count = 0
while count < books_count:
    if book_name != current_book:
        count += 1
        if count < books_count:
            current_book = input()
    else:
        print(f"You checked {count} books and found it.")
        break
if book_name != current_book:
    print(f"The book you search is not here!\nYou checked {count} books.")
