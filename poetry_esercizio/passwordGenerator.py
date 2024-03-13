import random

print("Welcome to your password generator")

chars = "qwertyuiopasdfghjklzxcvbnm,.-;:_é*èòà+ç#123654789/^?'ì!£$%&/()=?"

number = input("Amount of passwords to generate: ")
number=int(number)

length = input("Input your password length: ")
length = int(length)

print('\n Here are your passwords: ')

for pwd in range(number):
    passwords = ''
    for c in range(length):
        passwords+=random.choice(chars)
    print(passwords)