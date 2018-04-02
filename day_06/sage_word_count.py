import collections


def count_words(input_text):
    cnt = collections.Counter()
    for word in input_text:
        cnt[word] += 1
    print(cnt)
    most_common = cnt.most_common(10)
    # print(most_common)
    return most_common

def display_results(sorted_words):
    disp_res = list(enumerate(sorted_words, 1))
    # for word in disp_res:
    #     print(disp_res[0], disp_res[1][word])
    print(disp_res)

with open('illiad.txt', encoding='utf-8') as f:
    text = f.read()
    # print(text)
    normal_text = text.lower().split()
    # print(normal_text)
    counted_text = count_words(normal_text)
    print(counted_text)
    display_results(counted_text)
