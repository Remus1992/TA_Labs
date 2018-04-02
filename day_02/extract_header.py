# email_entry = input("Enter email address: ")
#
# header_first_list = email_entry.split('@')
#
# print(header_first_list)
#
# split_list_1 = header_first_list[-1]
#
# print(split_list_1)
#
# header_second_list = split_list_1.split('.')
#
# print(header_second_list)
#
# split_list_2 = header_second_list[0]
#
# print(split_list_2)


email_entry = input("Enter email address: ")

header_first_split = email_entry.split('@')[-1]

header_second_split = header_first_split.split('.')[0]

print(header_second_split)
