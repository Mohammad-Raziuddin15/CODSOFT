import random
import string

print("=====  STRONG PASSWORD GENERATOR  =====")

while True:

    length = int(input("\nEnter password length:-"))

    if length < 4:
        print("Password length should be at least 4")
        continue

    all_characters = string.ascii_letters + string.digits + string.punctuation

    password = " "

    for i in range(length):
        password += random.choice(all_characters)

    print("\nGenerated Password:", password)

    user_choice = input("\nDo you want to generate another password? (yes/no):-")

    if user_choice.lower() != "yes":
        print("\nPassword Generator closed")
        break



