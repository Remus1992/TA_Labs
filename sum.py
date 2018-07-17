# basic while loop
i = 0
s = 0
while i < 1000:
    if i % 3 == 0:
        s += i
    elif i % 5 == 0:
        s += i
    else:
        pass
    i += 1

print("Sum: %s" % s)

# list comprehension with built in functions
print(sum([x for x in range(1000) if x % 3 == 0 or x % 5 == 0]))
