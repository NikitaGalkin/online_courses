from datetime import datetime, timedelta, date 

input_text = input().split()
date1 = date(int(input_text[0]), int(input_text[1]), int(input_text[2]))

my_delta = timedelta(days = int(input()))

date2 = date1 + my_delta
print(date2.year, date2.month, date2.day)

