import datetime
#weekdays tuple
weekDays = ("Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday")
# retrieving current date
now = datetime.date.today()
# retrieve the day of the week which is an integer
dayOfWeek=now.weekday()
#subscript into weekDays using the dayOfWeek
today=weekDays[dayOfWeek]
#calculate and print days until the weekend
daysToWeekend=6-dayOfWeek
print("There are ", daysToWeekend-1,"days until the weekend")
quotePrinted="false"
for left in weekDays[dayOfWeek:daysToWeekend]:
    if today=="Sunday" and quotePrinted =="false":
        print("Accounting quiz is due Sunday!")
        quotePrinted="true"
    elif (today=="Monday" or today=="Tuesday" or today== "Wednesday") and quotePrinted=="false":
        print(left, "Back to the due dates of the week!")
        quotePrinted="true"
    elif today=="Thursday" and quotePrinted=="false":
        print(left, "Back to the due dates of the week!")
        quotePrinted="true"
    elif quotePrinted=="false":
        print(left, "Four due dates in my future!")
        quotePrinted="true"
    else:
        print(left)
        
