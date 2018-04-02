def get_distance():
    user_distance = float(input("Enter a distance: "))
    return user_distance


def get_units_of_distance():
    while True:
        units = input("Enter Units ('mi' for miles, 'km' for kilometers, 'ft' for feet, and 'm' for meters): ")
        if units == "mi" or units == "km" or units == "ft" or units == "m":
            return units
        else:
            print("Not a valid unit of distance.")


def get_target_unit(before_conversion_units):
    while True:
        after_conversion_units = input(
            "Enter Target Units ('mi' for miles, 'km' for kilometers, 'ft' for feet, and 'm' for meters): ")
        if after_conversion_units == before_conversion_units:
            print("Pick another unit. You already know that.")
        else:
            return after_conversion_units


def convert_distance(distance, units_of_distance, target_unit):
    if units_of_distance == 'mi':
        if target_unit == 'ft':
            # 1 mile to 5280 feet
            new_distance = distance * 5280
            print('%s %s' % (new_distance, target_unit))

        elif target_unit == 'km':
            # 1 mile = 1.60934 kilometers
            new_distance = distance * 1.60934
            print('%s %s' % (new_distance, units_of_distance))
        elif target_unit == 'm':
            # 1 mile = 1609.34 meters
            new_distance = distance * 1609.34
            print('%s %s' % (new_distance, units_of_distance))

    elif units_of_distance == 'km':
        if target_unit == 'm':
            # 1 kilometer to 1000 meters
            new_distance = distance * 1000
            print('%s %s' % (new_distance, units_of_distance))
        elif target_unit == 'mi':
            # 1 kilometer = 0.621371 miles
            new_distance = distance * 0.621371
            print('%s %s' % (new_distance, units_of_distance))
        elif target_unit == 'ft':
            # 1 kilometer = 3280.84 feet
            new_distance = distance * 3280.84
            print('%s %s' % (new_distance, units_of_distance))

    elif units_of_distance == 'ft':
        if target_unit == 'm':
            # 1 foot = 0.3048 meters
            new_distance = distance * 0.3048
            print('%s %s' % (new_distance, units_of_distance))
        elif target_unit == 'km':
            # 1 foot = 0.0003048 kilometers
            new_distance = distance * 0.0003048
            print('%s %s' % (new_distance, units_of_distance))
        elif target_unit == 'm':
            # 1 foot = 0.000189394 miles
            new_distance = distance * 0.000189394
            print('%s %s' % (new_distance, units_of_distance))

    elif units_of_distance == 'm':
        if target_unit == 'km':
            # 1 meter = 0.001 kilometer
            new_distance = distance * 0.001
            print('%s %s' % (new_distance, units_of_distance))
        elif target_unit == 'm':
            # 1 meter = 0.000621371 miles
            new_distance = distance * 0.000621371
            print('%s %s' % (new_distance, units_of_distance))
        elif target_unit == 'ft':
            # 1 meter = 3.28084 feet
            new_distance = distance * 3.28084
            print('%s %s' % (new_distance, units_of_distance))

    else:
        print('Not a valid option')


user_distance = get_distance()
user_units_of_distance = get_units_of_distance()
user_target_unit = get_target_unit(user_units_of_distance)

convert_distance(user_distance, user_units_of_distance, user_target_unit)
