def phone_entry():
    while True:
        raw_phone_number = input("Enter 10 digit phone number: ")
        if len(raw_phone_number) == 10:
            return raw_phone_number
        else:
            print('Can\'t you read?')


def fancy(phone_number):
    first_third = phone_number[0:3]
    # print(first_third)
    second_third = phone_number[3:6]
    # print(second_third)
    third_third = phone_number[6:]
    # print(third_third)
    fancy_number = "({}){}-{}".format(first_third, second_third, third_third)
    return fancy_number


number = phone_entry()
print(fancy(number))
