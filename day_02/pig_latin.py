# Lab: Pig Latin
###### Delivery Method: Prompt Only
#### Goal

# Create a program asks for a _single_ English word and translates it to **Pig Latin**.
# It prints out the input word and the resulting translation like the example below.

#### Instructions

# 1. If the first letter is a consonant, move it to the end.
# 1. Add "ay" to the end of that.
# 1. If the first letter is a vowel, just ad "yay" to the end.

# > Word? hat
# > hat in Pig Latin is athay
# > Word? apple
# > apple in Pig Latin is appleyay


# word = list('word')
# print(word)
# first = word[0]
# word.remove(first)
# print(word)
# word.append('a')
# print(word)


def pig_latin(word):
    pig_consonant = 'ay'
    pig_vowel = 'yay'

    split_word = list(word)
    print(split_word)
    first = split_word[0]
    print(first)
    if first == "a" or first == "e" or first == "i" or first == "o" or first == "u":
        final_word = word + pig_vowel
        print(final_word)

    else:
        split_word.remove(first)
        print(split_word)
        split_word.append(first)
        print(split_word)
        second_word = ''
        joined_word = second_word.join(split_word)
        print(joined_word)
        final_word = joined_word + pig_consonant
        print(final_word)


original_word = input('Enter your word here: ')
pig_latin(original_word)
