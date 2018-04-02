# import math
#
# width_wall = float(input("Width of wall: "))
# height_wall = float(input("Height of wall: "))
# coats = float(input("How many coats: "))
# paint_per_gallon = 400
# gallon_cost = float(input("Gallon cost: "))
#
# surface_area_wall = width_wall * height_wall
# total_surface_area = surface_area_wall * coats
#
#
# gallons_needed = math.ceil(total_surface_area / paint_per_gallon)
# total_gallon_cost = gallons_needed * gallon_cost
#
# print("Area Wall: %s" % surface_area_wall)
# print("Gallons needed: %s" % gallons_needed)
# print("Total Cost of Paint: %s" % total_gallon_cost)

import math

# # width_wall = float(input("Width of wall: "))
# # height_wall = float(input("Height of wall: "))
# coats = float(input("How many coats: "))
# paint_per_gallon = 400
# gallon_cost = float(input("Gallon cost: "))
#
# surface_area_wall = width_wall * height_wall
# total_surface_area = surface_area_wall * coats
#
#
# gallons_needed = math.ceil(total_surface_area / paint_per_gallon)
# total_gallon_cost = gallons_needed * gallon_cost
#
# print("Area Wall: %s" % surface_area_wall)
# print("Gallons needed: %s" % gallons_needed)
# print("Total Cost of Paint: %s" % total_gallon_cost)


walls = {
    # 'living_room_west': {'height': 200, 'width': 600},
}


def new_wall():
    wall_name = input("Enter Wall Name (sample: living_room_west: ").lower()
    width_wall = float(input("Width of wall: "))
    height_wall = float(input("Height of wall: "))
    surface_area_wall = width_wall * height_wall
    walls[wall_name] = {'name': wall_name, 'width': width_wall, 'height': height_wall,
                        'surface_area': surface_area_wall}
    return

def edit_wall(amendment):
    del walls[amendment]
    wall_name = input("Enter Wall Name (sample: living_room_west: ").lower()
    width_wall = float(input("Width of wall: "))
    height_wall = float(input("Height of wall: "))
    surface_area_wall = width_wall * height_wall
    walls[wall_name] = {'name': wall_name, 'width': width_wall, 'height': height_wall,
                        'surface_area': surface_area_wall}
    return


def delete_wall(excise):
    del walls[excise]
    return


def print_walls():
    for i in walls:
        print('{}:\n\t{}\n\t{}\n\t{}'.format(walls[i]['name'], walls[i]['width'], walls[i]['height'], walls[i]['surface_area']))


def gallon_total(num_coats, paint_p_gallon, cost_per_gallon):
    surface_area_list = []
    for i in walls:
        surface_area_list.append(walls[i]['surface_area'])
        print(surface_area_list)

    total_surface_area = sum(surface_area_list)
    print("Total Surface Area: %s" % total_surface_area)
    total_surface_area_paint = total_surface_area * num_coats
    gallons_needed = math.ceil(total_surface_area_paint / paint_p_gallon)
    print("Gallons Needed: %s" % gallons_needed)
    total_gallon_cost = gallons_needed * cost_per_gallon
    print("Total Gallon Cost: %s" % total_gallon_cost)


def command_line_prompt():
    while True:
        print('1. Add a Wall (new)')
        print('2. Edit a Wall (edit)')
        print('3. Remove a Wall (delete)')
        print('4. Print Directory (directory)')
        print('5. Total Costs (sa)')
        print('6. Quit (quit)')
        # print('Do you wish to add a new contact (new), search for a contact (search), edit an existing contact (edit), or delete a contact (delete)?: ')
        option = input().lower()
        # if option in 'new search edit delete'.split()
        if option == 'new' or option == '1':
            new_wall()
        elif option == 'edit' or option == '2':
            a = input("what is the last name of the person you are wanting to edit?: ").title()
            edit_wall(a)
        elif option == 'delete' or option == '3':
            x = input("what is the last name of the person you are wanting to delete?: ").title()
            delete_wall(x)
        elif option == 'directory' or option == '4':
            print_walls()
        elif option == 'sa' or option == '5':
            coats = float(input("How many coats: "))
            paint_per_gallon = 400
            gallon_cost = float(input("Gallon cost: "))
            gallon_total(coats, paint_per_gallon, gallon_cost)
        elif option == 'quit' or option == '6':
            break
        else:
            print('Please enter your option exclusively as either "new" or "search" or "edit" or "delete".')


command_line_prompt()
