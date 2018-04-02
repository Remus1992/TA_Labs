# Pick Six Lottery Machine
import random


def generateWinningNumbers():
    data = []
    count = 0
    while count < 6:
        num = random.randint(1, 99)
        data.append(num)
        count += 1
    # print(winningList)
    return data


# def generateTicketNumbers():
#     ticketList = []
#     count = 0
#     while count < 6:
#         num = random.randint(1, 10)
#         ticketList.append(num)
#         count += 1
#     # print(ticketList)
#     return ticketList


def compareLists(winning_set, ticket_set):
    iteration_set = 0
    match = 0
    while iteration_set < 6:
        if winning_set[iteration_set] == ticket_set[iteration_set]:
            # print('Match')
            match += 1
        # else:
        #     pass
        # print('Sorry')
        iteration_set += 1
    return match


def ticketWinningAmount(number_matches): # matching_amount
    ticket_balance = 0
    if number_matches == 1:
        ticket_balance += 4
        return ticket_balance
    elif number_matches == 2:
        ticket_balance += 7
        return ticket_balance
    elif number_matches == 3:
        ticket_balance += 100
        return ticket_balance
    elif number_matches == 4:
        ticket_balance += 50000
        return ticket_balance
    elif number_matches == 5:
        ticket_balance += 1000000
        return ticket_balance
    elif number_matches == 6:
        ticket_balance += 25000000
        print("You got the lucky numbers!")
        return ticket_balance
    else:
        return ticket_balance


iter = 0
balance = 0
matching_amount = 0
while iter < 100000:
    balance -= 2
    winning_numbers = generateWinningNumbers() # winningList
    ticket_numbers = generateWinningNumbers() # winningList
    matching_amount = compareLists(winning_numbers, ticket_numbers) # match
    ticketwinnings = ticketWinningAmount(matching_amount) # ticket_balance
    # print(type(ticketwinnings))
    # print(type(balance))
    balance += ticketwinnings
    print(balance)
    iter += 1

print("After 10,000 tickets processed, your balance is: %s" % balance)
