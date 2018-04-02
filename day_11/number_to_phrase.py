num_words_1 = {
    1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five',
    6: 'six', 7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten', 11: 'eleven',
    12: 'twelve', 13: 'thirteen', 14: 'fourteen', 15: 'fifteen',
    16: 'sixteen', 17: 'seventeen', 18: 'eighteen', 19: 'nineteen',
    0: ''
}

num_words_2 = {
                2: 'twenty', 3: 'thirty', 4: 'forty', 5: 'fifty', 6: 'sixty', 7: 'seventy',
              'eighty', 'ninety'
}


num_words_3 = {
    1: 'one hundred', 2: 'two hundred', 3: 'three hundred',
    4: 'four hundred', 5: 'five hundred', 6: 'six hundred',
    7: 'seven hundred', 8: 'eight hundred', 9: 'nine hundred'
}

user_number = int(input('Give me a number between 0 and 99 to convert: '))
hundreds_digit = user_number // 100
print("Hundreds: %s" % hundreds_digit)
tens_digit = (user_number % 100 // 10)
print("Tens: %s" % tens_digit)
ones_digit = user_number % 100 % 10
# print("Ones: %s" % tens_digit)

if hundreds_digit > 0:
    if tens_digit <= 0 and ones_digit == 0:
        print(num_words_3[hundreds_digit])
    else:
        print(
            num_words_3[hundreds_digit],
            num_words_2[tens_digit],
            num_words_1[ones_digit]
        )

else:
    if user_number == 0:
        print("ZERO")
    elif user_number >= 1 and user_number < 20:
        print(num_words_1[user_number])
    elif user_number > 19 and user_number < 100:
        print(num_words_2[tens_digit], num_words_1[ones_digit])
    # elif user_number > 99 and user_number < 1000:
    #     if tens_digit <= 0 and ones_digit == 0:
    #         print(num_words_3[hundreds_digit])
    #     else:
    #         print(
    #             num_words_3[hundreds_digit],
    #             num_words_2[tens_digit],
    #             num_words_1[ones_digit]
    #         )
