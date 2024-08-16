#Password Generator
import random
number = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
letter = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
symbol = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '<', '>', '/', '?', '|', '+' ]
password_list = []
number_of_number = int(input("How many numbers do you want:\n"))
number_of_letter = int(input("How many letters do you want:\n"))
number_of_symbol = int(input("How many symbols do you want:\n"))
for char in range(1, number_of_number+1):
    password_list += random.choice(number)
for char in range(1, number_of_symbol+1):
    password_list += random.choice(symbol)
for char in range(1, number_of_letter+1):
    password_list += random.choice(letter)
random.shuffle(password_list)
password = ''
for char in password_list:
    password += char
print(password)