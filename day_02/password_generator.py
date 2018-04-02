import random

lowercase_characters = [
    "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w",
    "x", "y", "z"
]

uppercase_characters = [
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W',
    'X', 'Y', 'Z'
]

numbers = [
    "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"
]

special_characters = [
    "#", "*", "£", "$", "+", "!", "@", "$", "&", "^"
]


# def getLength():
#     length = int(input('How long would you like your password to be?: '))
#     return length


def getLowercase():
    lowercase_amount = int(input('How many lowercase letters would you like?: '))
    return lowercase_amount


def getUppercase():
    uppercase_amount = int(input('How many uppercase letters would you like?: '))
    return uppercase_amount


def getNumbers():
    uppercase_amount = int(input('How many numbers would you like?: '))
    return uppercase_amount


def getSpecialCharaceters():
    special_characters_amount = int(input('How many special characters would you like?: '))
    return special_characters_amount


# def generateLetterList(length_password):
#     password_list = []
#     while length_password != 0:
#         letter = random.choice(password_characters)
#         # print(letter)
#         password_list.append(letter)
#         # print(password_list)
#         length_password -= 1
#     return password_list

def generateLowercaseLettersList(lowercase_amount):
    lowercase_list = []
    while lowercase_amount != 0:
        letter = random.choice(lowercase_characters)
        # print(letter)
        lowercase_list.append(letter)
        # print(password_list)
        lowercase_amount -= 1
    return lowercase_list


def generateUppercaseLettersList(uppercase_amount):
    uppercase_list = []
    while uppercase_amount != 0:
        letter = random.choice(uppercase_characters)
        # print(letter)
        uppercase_list.append(letter)
        # print(password_list)
        uppercase_amount -= 1
    return uppercase_list


def generateNumbersList(number_amount):
    number_list = []
    while number_amount != 0:
        letter = random.choice(numbers)
        # print(letter)
        number_list.append(letter)
        # print(password_list)
        number_amount -= 1
    return number_list


def generateSpecialCharacterList(special_character_amount):
    special_character_list = []
    while special_character_amount != 0:
        letter = random.choice(special_characters)
        # print(letter)
        special_character_list.append(letter)
        # print(password_list)
        special_character_amount -= 1
    return special_character_list


def compileList(list_of_letters):
    password = ''
    joined_password = password.join(list_of_letters)
    return joined_password


# user_defined_length = getLength()
user_lowercase_amount = getLowercase()
user_uppercase_amount = getUppercase()
user_number_amount = getNumbers()
user_special_character_amount = getSpecialCharaceters()

list_lowercase = generateLowercaseLettersList(user_lowercase_amount)
# print(list_lowercase)
list_uppercase = generateUppercaseLettersList(user_uppercase_amount)
# print(list_uppercase)
list_numbers = generateNumbersList(user_number_amount)
# print(list_numbers)
list_special_characters = generateSpecialCharacterList(user_special_character_amount)
# print(list_special_characters)

total_password_list = list_lowercase + list_uppercase + list_numbers + list_special_characters
random.shuffle(total_password_list)
print(compileList(total_password_list))

# list_letters = generateLetterList(user_defined_length)
# print(compileList(list_letters))
