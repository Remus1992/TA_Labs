print("Change Calculator")

twenty_dollar = 2000
ten_dollar = 1000
five_dollar = 500
one_dollar = 100
quarter = 25
dime = 10
nickel = 5
penny = 1

citem = input("How much did the item cost?: ")
money_given = input("Enter how much money given: ")
money_given = int(float(money_given) * 100)
# print(money_given)
citem = int(float(citem) * 100)
# print(citem)
money_back = money_given - citem
# print(money_back)


twenty_mb = money_back // twenty_dollar
partial_total = money_back - twenty_mb * twenty_dollar
ten_mb = partial_total // ten_dollar
ten_partial_total = partial_total - ten_mb * ten_dollar
five_mb = ten_partial_total // five_dollar
five_partial_total = ten_partial_total - five_mb * five_dollar
one_mb = five_partial_total // one_dollar
one_partial_total = five_partial_total - one_mb * one_dollar
qmb = one_partial_total // quarter
qpartial_total = one_partial_total - qmb * quarter
dmb = qpartial_total // dime
dpartial_total = qpartial_total - dmb * dime
nmb = dpartial_total // nickel
npartial_total = dpartial_total - nmb * nickel
pmb = npartial_total // penny
ppartial_total = npartial_total - pmb * penny

print("You need %s 20-dollar bills, %s 10-dollar bills, %s 5-dollar bills, %s 1-dollar bills, %s quarters, %s dimes, %s nickels, %s pennies." % (twenty_mb, ten_mb, five_mb, one_mb, qmb, dmb, nmb, pmb))

# a = 0.25
# b = 0.55/a
# print(b)
#
# c = 0.25
# d = 0.55//c
# print(d)