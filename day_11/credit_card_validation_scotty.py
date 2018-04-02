def check_card_validation():
    # card_input = list(input('Enter the cc number:\n'))
    card_input = '1234567812345678'
    converted_num = []
    for num in card_input:
        converted_num.append(int(num))
    print(converted_num)
    check_digit = converted_num.pop()
    print(check_digit)
    # del converted_num[-1]
    print(converted_num)
    converted_num.reverse()
    print(converted_num)
    for i in range(len(converted_num)):
        if i % 2 == 0:
            converted_num[i] *= 2
    print(converted_num)
    return converted_num, check_digit


print(check_card_validation())
