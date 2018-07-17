# def check_card_validation():
#     # card_input = list(input('Enter the cc number:\n'))
#     card_input = '4556737586899855'
#     converted_num = []
#     for num in card_input:
#         converted_num.append(int(num))
#     print(converted_num)
#     check_digit = converted_num.pop()
#     print(check_digit)
#     # del converted_num[-1]
#     print(converted_num)
#     converted_num.reverse()
#     print(converted_num)
#     for i in range(len(converted_num)):
#         if i % 2 == 0:
#             converted_num[i] *= 2
#     print(converted_num)
#
#     return converted_num, check_digit
#
#
# check_card_validation()

# Validate credit card number "4556737586899855"


# This method does not work for all credit cards.
# It employs the Luhn Algorithm which will validate specific brands of cards


def validate_credit_card(s):
    # converts string to a list of integers
    list_card_int = list(map(int, list(s)))

    # removes final digit for later verification
    final_value = list_card_int[-1]
    list_card_int.pop()
    # reverses list
    reversed_list = list(reversed(list_card_int))
    # doubles every other item
    for x in range(len(reversed_list)):
        if x % 2 == 0:
            reversed_list[x] *= 2
    doubled = reversed_list
    print(doubled)
    # subtracts 9 from every number greater than 9
    for x in range(len(doubled)):
        if doubled[x] > 9:
            doubled[x] -= 9
    subtracted_num = doubled
    # takes the sum of all of the numbers in the list
    summed = sum(subtracted_num)
    # converts integer to a string and strips final digit
    str_sd = str(summed)
    str_sd.strip()
    second_num_str = str_sd[-1]
    # converts back to integer
    second_num = int(second_num_str)
    # finally checks the final digit produced with the final digit of the original set of data
    # if they are equal, then the card is a valid CC number according to the Luhn Algorithm
    if final_value == second_num:
        print("Valid Credit Card Number")
    else:
        print("Invalid Credit Card Number")


card_number = "4556737586899855"

validate_credit_card(card_number)
