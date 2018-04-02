import math
import string

ARI_SCALE = {
     1: {'ages':   '5-6', 'grade_level': 'Kindergarten'},
     2: {'ages':   '6-7', 'grade_level':    '1st Grade'},
     3: {'ages':   '7-8', 'grade_level':    '2nd Grade'},
     4: {'ages':   '8-9', 'grade_level':    '3rd Grade'},
     5: {'ages':  '9-10', 'grade_level':    '4th Grade'},
     6: {'ages': '10-11', 'grade_level':    '5th Grade'},
     7: {'ages': '11-12', 'grade_level':    '6th Grade'},
     8: {'ages': '12-13', 'grade_level':    '7th Grade'},
     9: {'ages': '13-14', 'grade_level':    '8th Grade'},
    10: {'ages': '14-15', 'grade_level':    '9th Grade'},
    11: {'ages': '15-16', 'grade_level':   '10th Grade'},
    12: {'ages': '16-17', 'grade_level':   '11th Grade'},
    13: {'ages': '17-18', 'grade_level':   '12th Grade'},
    14: {'ages': '18-22', 'grade_level':      'College'}
}
wordcount = {}

word_total = 0
with open('huckfinn.txt', encoding="utf8") as file:
    file_string = file.read()


file_words = file_string
file_characters = file_string
file_sentences = file_string

for word in file_words.split():
    word = word.lower()
    if word not in wordcount:
        wordcount[word] = 1
        word_total += 1
    else:
        wordcount[word] += 1
        word_total += 1

character_string = file_characters.replace(' ', '')
character_string_02 = character_string.replace('\t', '')
character_string_03 = character_string_02.replace('\n', '')
character_string_04 = character_string_03.replace('.', '')
character_string_05 = character_string_04.replace(',', '')
character_string_06 = character_string_05.replace(';', '')
character_string_07 = character_string_06.replace(':', '')
character_string_08 = character_string_07.replace('-', '')

num_characters = len(character_string_03)
print("Number of Characters:\t{}".format(len(character_string_08)))

# characters = ''.join(ch if ch in string.ascii_letters else ' ' for ch in file_sentences).split()#file_sentences.maketrans('', '', string.punctuation)''

sentences = ''
for i in file_sentences:
    if i in '.!?':
        sentences += '<EndSentence>'
    else:
        sentences += i

num_sentences = len(sentences.split('<EndSentence>'))
print(sentences)
# sentences = file_sentences.split('.')
# for sentence in sentences:
#     if "?" is in sentence:
#         sentence.split('?')

# print(sentences)
# num_sentences = len(sentences)
print("Number of Sentences:\t{}".format(num_sentences))
print("Number of Words:\t\t{}".format(word_total))

ARI_text = math.ceil((4.71 * (num_characters / word_total)) + (0.5 * (word_total / num_sentences)) - 21.43)
print("ARI:\t\t\t\t\t{}".format(ARI_text))

for ARI in ARI_SCALE:
    if ARI == ARI_text:
        print(
            """
            The ARI for {} is {}
            This corresponds to a {} of difficulty
            that is suitable for an average person {} years old.
            """.format('huckfinn.txt', ARI, ARI_SCALE[ARI]['grade_level'], ARI_SCALE[ARI]['ages'])
            )