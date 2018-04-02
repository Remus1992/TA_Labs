from random import randint


def pick6_lottery():
    n1 = randint(1, 9)
    n2 = randint(1, 9)
    n3 = randint(1, 9)
    n4 = randint(1, 9)
    n5 = randint(1, 9)
    n6 = randint(1, 9)
    return n1, n2, n3, n4, n5, n6


# n1, n2, n3, n4, n5, n6 = pick6_lottery()
# print(n1, n2, n3, n4, n5, n6)

def user_picks():
    up1 = randint(1, 9)
    up2 = randint(1, 9)
    up3 = randint(1, 9)
    up4 = randint(1, 9)
    up5 = randint(1, 9)
    up6 = randint(1, 9)
    return up1, up2, up3, up4, up5, up6


# up1, up2, up3, up4, up5, up6 = user_picks()
# print(up1, up2, up3, up4, up5, up6)


def check_matches(up1, up2, up3, up4, up5, up6, n1, n2, n3, n4, n5, n6):
    matches = 0
    if n1 == up1:
        matches += 1
    if n2 == up2:
        matches += 1
    if n3 == up3:
        matches += 1
    if n4 == up4:
        matches += 1
    if n5 == up5:
        matches += 1
    if n6 == up6:
        matches += 1
    return matches


# print('matches: %s' % matches)

for i in range(10):
    up1, up2, up3, up4, up5, up6 = user_picks()
    print(up1, up2, up3, up4, up5, up6)
    n1, n2, n3, n4, n5, n6 = pick6_lottery()
    print(n1, n2, n3, n4, n5, n6)
    matches = check_matches(up1, up2, up3, up4, up5, up6, n1, n2, n3, n4, n5, n6)
    print(matches)
