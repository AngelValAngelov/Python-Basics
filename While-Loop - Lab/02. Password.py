username = input()
password = input()
pass_input = input()

while password != pass_input:
    pass_input = input()

print(f"Welcome {username}!")