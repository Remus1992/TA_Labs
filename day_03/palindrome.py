def get_word():
    word = input('What word would you like to try out?: ')
    return word


def palindrome(first_word):
    list_word = list(first_word)
    print(list_word)
    list_word.reverse()
    # print(list_word)
    temp_word = ''
    second_word = temp_word.join(list_word)
    # print(second_word)
    if second_word == first_word:
        print("Palindrome!")
    else:
        print("sorry.")


testing_word = get_word()
palindrome(testing_word)
