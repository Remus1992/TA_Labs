# time = input("Enter the time of the day in military time: ")
# split_time = time.split(":")
#
# print(split_time)
#
# integer = int(split_time[0])
# if integer in range(6, 10):
#    print("Breakfast")
#
# elif split_time[0] in range(11, 15):
#    print("Lunch")
#
# elif split_time in range(18, 22):
#    print("Dinner")
#
# elif split_time in range(21, 25):
#    print("Hammertime")
#
# elif split_time in range(0, 5):
#    print("Hammertime")

# Hammer Time

meal_time = input("Enter a time of day in the following format (5:00 PM): ")
meridian_split = meal_time.split(' ')
meridian_id = meridian_split[1]


# print(meridian_id)


def meridian(am_pm):
    day_time = int(meridian_split[0].replace(':', ''))
    print(day_time)
    if am_pm == 'PM':
        day_time += 1200
        schedule(day_time)
        # print('PM')
    elif am_pm == 'AM':
        schedule(day_time)
        # print('AM')
    else:
        print('invalid format')


def schedule(time):
    print(time)
    if time in range(600, 1000):
        print("Breakfast")

    elif time in range(1100, 1500):
        print("Lunch")

    elif time in range(1800, 2200):
        print("Dinner")

    elif time in range(2100, 2500) or time in range(0, 500):
        print("Hammertime")

    else:
        print('Not a meal time')


meridian(meridian_id)
