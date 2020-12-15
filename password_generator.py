import random


def pass_word_generator():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
               'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
    print("Welcome to the PyPassword Generator!")
    users_letters = int(input("How many letters would you like in your password?\n"))
    users_symbols = int(input(f"How many symbols would you like?\n"))
    users_numbers = int(input(f"How many numbers would you like?\n"))
    password = []
    for letter in range(users_letters):
        a = random.choice(letters)
        password.append(a)
    for symbol in range(users_symbols):
        b = random.choice(symbols)
        password.append(b)
    for number in range(users_numbers):
        c = random.choice(numbers)
        password.append(c)
    random.shuffle(password)
    final_password = ""
    for char in password:
        final_password += char
    print(f"Your Password is: {final_password}\nMake sure to write it down somewhere save")
    print()


pass_word_generator()
while True:
    print("Would you like to generate a new password? Enter y to generate a new on or x to exit.")
    new_password = input().casefold()
    if new_password == 'y':
        pass_word_generator()
    else:
        break
