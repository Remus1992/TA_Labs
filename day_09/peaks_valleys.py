data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]

# print(len(data))
def peaks(data):
    y = 1
    for i in range(1, len(data) - 1):
        if data[i-1] < data[i] and data[i] > data[i+1]:
            before = i-1
            after = i+1
            print("Position {} is a peak. BEFORE: {}, AFTER: {}".format(y, before, after))
            y += 1

        else:
            y += 1


def valleys(data):
    pass


def peaks_and_valleys(data):
    pass


peaks(data)
valleys(data)
peaks_and_valleys(data)
