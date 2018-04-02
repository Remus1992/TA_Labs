 # password_gen.py

import random

characters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789_&%$#@!'
password = ''

def welcome():
    print('This is a password generator!')
    print('Remember, a strong password should contain at least 8 characters')
    while True:
        length = int(input('How many charaters would you like your password to be?: '))
        if length >= 8:
            return length
        else:
            print('You must choose a minimum of 8 characters')

def generate():
    for i in range(length):
        password += random.choice(characters)
    print(password)

user_length = welcome()
print(user_length)