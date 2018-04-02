import csv

phonebook = {
    # 'jones': {'first_name': 'Chris', 'last_name': 'Jones', 'phone_number': '5412813629'},
    'Remus': {
        'first_name': 'Remington',
        'last_name': 'Henderson',
        'phone_number': {
            'fancy_phone': '(541)281-3629',
            'standard_phone': '5412813629'
        }
    },
    # 'Cort': {'first_name': 'Cortland',
    #          'last_name': 'Henderson',
    #          'phone_number': {
    #              'fancy_phone': '(541)281-3627',
    #              'standard_phone': '5412813627'
    #          }
    #          }
}

# phonenumber[user]['phone_number']['standard_phone']
# for user in phonebook:
#     for phone_dict in phonebook[user]:
#         if phone_dict == 'phone_number':
#             for number in phonebook[user][phone_dict]:
#                 if number == 'standard_phone':
#                     print(phonebook[user][phone_dict][number])

def new_entry():
    new_nick_name = input("Give a unique nickname (character sensitive): ")
    new_first_name = input("Enter New First Name: ").title()
    new_last_name = input("Enter New Last Name: ").title()
    # raw_phone_number = int(input("Enter New Phone Number: "))
    while True:
        raw_phone_number = input("Enter 10 digit phone number: ")
        if len(raw_phone_number) == 10:
            first_third = raw_phone_number[0:3]
            # print(first_third)
            second_third = raw_phone_number[3:6]
            # print(second_third)
            third_third = raw_phone_number[6:]
            # print(third_third)
            fancy_number = "({}){}-{}".format(first_third, second_third, third_third)
            phonebook[new_nick_name] = {'first_name': new_first_name,
                                        'last_name': new_last_name,
                                        'phone_number': {
                                            'fancy_phone': fancy_number,
                                            'standard_phone': raw_phone_number
                                        }
                                        }
            return
        else:
            print('Can\'t you read?')

# phonenumber[user]['phone_number']['standard_phone']
# phonenumber[user]['first_name']
# phonenumber[user]['last_name']

def search_entry(query):
    for user in phonebook:
        for item in phonebook[user]:
            if item == 'phone_number':
                for style_number in phonebook[user][item]:
                    if style_number == 'standard_phone':
                        if query in phonebook[user][item][style_number]:
                            print('\tFull Name: {} {}'.format(phonebook[user]['first_name'],
                                                            phonebook[user]['last_name']))
                            print('\t\tPhone: {}'.format(phonebook[user]['phone_number']['fancy_phone']))
    for user in phonebook:
        for item in phonebook[user]:
            if item == 'first_name':
                if query in phonebook[user][item].lower():
                    print('\tFull Name: {} {}'.format(phonebook[user]['first_name'],
                                                      phonebook[user]['last_name']))
                    print('\t\tPhone: {}'.format(phonebook[user]['phone_number']['fancy_phone']))
    for user in phonebook:
        for item in phonebook[user]:
            if item == 'last_name':
                if query in phonebook[user][item].lower():
                    print('\tFull Name: {} {}'.format(phonebook[user]['first_name'],
                                                      phonebook[user]['last_name']))
                    print('\t\tPhone: {}'.format(phonebook[user]['phone_number']['fancy_phone']))


    # try:
    #     print('Full Name: {} {}'.format(phonebook[query]['first_name'], phonebook[query]['last_name']))
    #     print('Phone: {}'.format(phonebook[query]['phone_number']['fancy_phone']))
    # except KeyError:
    #     print("That is Not a Valid Entry.")


def edit_entry(amendment):
    # del phonebook[amendment]
    new_first_name = input("Enter New First Name: ").title()
    new_last_name = input("Enter New Last Name: ").title()
    while True:
        raw_phone_number = input("Enter 10 digit phone number: ")
        if len(raw_phone_number) == 10:
            first_third = raw_phone_number[0:3]
            # print(first_third)
            second_third = raw_phone_number[3:6]
            # print(second_third)
            third_third = raw_phone_number[6:]
            # print(third_third)
            fancy_number = "({}){}-{}".format(first_third, second_third, third_third)

            dict = {'first_name': new_first_name, 'last_name': new_last_name, 'phone_number': fancy_number, 'standard_phone': raw_phone_number}
            phonebook[amendment].update(dict)
            return
        else:
            print('Can\'t you read?')


def delete_contact(excise):
    del phonebook[excise]
    return


def print_directory():
    # print(phonebook)
    for i in phonebook:
        print('Full Name: {} {} - Phone Number: {}'.format(phonebook[i]['first_name'], phonebook[i]['last_name'],
                                                           phonebook[i]['phone_number']['fancy_phone']))


def command_line_prompt():
    while True:
        print('1. Add a Contact (new)')
        print('2. Lookup a Contact (search)')
        print('3. Edit a Contact (edit)')
        print('4. Remove a Contact (delete)')
        print('5. Print Directory (directory)')
        print('6. Quit (quit)')
        # print('Do you wish to add a new contact (new), search for a contact (search), edit an existing contact (edit), or delete a contact (delete)?: ')
        option = input().lower()
        # if option in 'new search edit delete'.split()
        if option == 'new' or option == '1':
            new_entry()
        elif option == 'search' or option == '2':
            q = input("Enter First Name, Last Name, or Phone Number: ").lower()
            search_entry(q)
        elif option == 'edit' or option == '3':
            a = input("what is the nickname of the person you are wanting to edit?: ").lower()
            edit_entry(a)
        elif option == 'delete' or option == '4':
            x = input("what is the nickname of the person you are wanting to delete?: ").lower()
            delete_contact(x)
        elif option == 'directory' or option == '5':
            print_directory()
        elif option == 'quit' or option == '6':
            break
        else:
            print('Please enter your option exclusively as either "new" or "search" or "edit" or "delete".')


command_line_prompt()
