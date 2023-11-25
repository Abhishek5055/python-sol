import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")

total_length = int(input("How long would you like your password to be?\n"))

nr_letters = int(input(f"How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# Calculate how many characters are left for letters, symbols, and numbers
remaining_length = total_length - (nr_letters + nr_symbols + nr_numbers)

# Ensure that the sum of specified characters doesn't exceed the total length
if remaining_length < 0:
    print("The total specified length exceeds the desired password length.")
else:
    password_list = []

    for _ in range(nr_letters):
        password_list.append(random.choice(letters))

    for _ in range(nr_symbols):
        password_list.append(random.choice(symbols))

    for _ in range(nr_numbers):
        password_list.append(random.choice(numbers))

    # Add remaining characters to the password list
    for _ in range(remaining_length):
        password_list.append(random.choice(letters + symbols + numbers))

    # Shuffling the password elements to mix the characters
    random.shuffle(password_list)

    # Converting the list of characters to a string
    password = ''.join(password_list)

    print(f"Your generated password is: {password}")
