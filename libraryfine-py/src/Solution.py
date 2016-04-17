#!/bin/python3

from datetime import date

d1, m1, y1 = input().strip().split(' ')
d1, m1, y1 = [int(d1), int(m1), int(y1)]
d2, m2, y2 = input().strip().split(' ')
d2, m2, y2 = [int(d2), int(m2), int(y2)]

result = 0
return_date = date(y1, m1, d1)
expect_date = date(y2, m2, d2)

# no fine if return before expect date
if return_date < expect_date:
    result = 0
# fine = 10,000 if more than 1 year late
elif return_date.year > expect_date.year:
    result = 10000
# fine = 500 * (months late) if more than 1 month late
elif return_date.month > expect_date.month:
    result = (return_date.month - expect_date.month) * 500
# fine = 15 * (days late) if more than 1 day late
elif return_date.day > expect_date.day:
    result = (return_date.day - expect_date.day) * 15

print(result)
