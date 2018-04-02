import random

emoticon_eyes = [':', ';', '>:', '|;', 'O:', '%', '#']
emoticon_noses = ['-', '', '^']
emoticon_mouths = [')', '(', 'X', '|', 'P', '/']


i = 5
while i != 0:
    emoticon = random.choice(emoticon_eyes) + random.choice(emoticon_noses) + random.choice(emoticon_mouths)
    print(emoticon)
    i -= 1
