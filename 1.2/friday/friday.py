"""
ID: giliev91
LANG: PYTHON3
TASK: friday
"""
with open("friday.in", "r") as f:
    N = int(f.readline().strip())

days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
thirteents = [0 for _ in range(7)]
date = [1, 1, 1900, 0]

while date[2] < (1900 + N):
    # print(date)
    day, month, year, dow = date

    # leap
    leap = True if year % 4 == 0 else False
    if leap and year % 100 == 0 and year % 400 != 0:
        leap = False

    # days
    day += 1
    dow = (dow + 1) % 7
    if day == 13:
        thirteents[dow] += 1

    if day > days_in_month[month - 1]:
        if month == 2 and leap and day == 29:
            pass
        else:
            day = 1
            month += 1

    # months
    if month == 13:
        month = 1
        year += 1

    date = [day, month, year, dow]

# rearrange for week start at saturday
thirteents = thirteents[5:] + thirteents[:5]
with open("friday.out", "w") as f:
    f.write(" ".join(map(str, thirteents)) + "\n")
