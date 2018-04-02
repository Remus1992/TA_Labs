# Version 1
# nums = [5, 0, 8, 3, 4, 1, 6]
#
# sum = 0
# for num in nums:
#     sum += num
#
# print(sum / len(nums))

# Version 2
nums = []
while True:
    num = input("Enter a number, or 'done': ")
    if num == 'done':
        break
    elif num.isalpha():
        print("That's not a number")
    else:
        num = int(num)
        nums.append(num)
        print(nums)

sum_list = sum(nums)
print('Average: %s' % sum_list)
