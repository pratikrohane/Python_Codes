#Convert Days into year-month-week-day

days=int(input())

years =(int) (days / 365)
remaining_days = days % 365
months =(int) (remaining_days / 30)
remaining_days = remaining_days % 30
weeks =(int) (remaining_days / 7)
remaining_days = remaining_days % 7
day = remaining_days

print("Years:", years, "Months:", months, "Weeks:", weeks, "Days:", day)