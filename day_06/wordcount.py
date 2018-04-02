import operator

wordcount = {}

with open('huckfinn.txt', encoding="utf8") as file:
    for word in file.read().split():
        word = word.lower()
        if word not in wordcount:
            wordcount[word] = 1
        else:
            wordcount[word] += 1

print(wordcount)
sorted_wordcount = sorted(wordcount.items(), key=operator.itemgetter(1), reverse=True)
print(sorted_wordcount)


for x in sorted_wordcount[:5]:
    print(x)
