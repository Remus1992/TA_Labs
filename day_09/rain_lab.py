import datetime
import operator
import matplotlib.pyplot as plt

with open("hayden_island.rain.txt", 'r') as f:
    content = f.readlines()
# you may also want to remove whitespace characters like `\n` at the end of each line
content = [x.strip() for x in content]
print(content)

weather = {}

i = 0
for day in content:
    row = content[i].split()
    # print(row)
    date_raw = row[0]
    # print(row[0])
    if row[1] == '-':
        total_rain = 0
    else:
        total_rain = int(row[1])
    # print(total_rain)

    date = datetime.datetime.strptime(date_raw, '%d-%b-%Y')
    # print(date.year)  # 2016
    # print(date.month)  # 3
    # print(date.day)  # 25
    # print(date)  # 2016-03-25 00:00:00
    # print(date.strftime('%d-%b-%Y'))  # 25-Mar-2016

    weather[date_raw] = total_rain

    i += 1

print(weather)
sorted_dates = sorted(weather.items(), key=operator.itemgetter(0), reverse=True)
print(sorted_dates)

average = sum([pair[1] for pair in sorted_dates]) / len(weather)
print(average)

day = [x[0] for x in sorted_dates[:100]]
value = [x[1] for x in sorted_dates[:100]]
plt.plot(day, value)
plt.show()
