import datetime

hrs = datetime.datetime.now().hour
print(datetime.datetime.now())

if hrs >= 0 and hrs < 12:
    print("Good Morning Sachit")
elif hrs >= 12 and hrs < 18:
    print("Good Afternoon Sachit")
else:
    print("Good Evening Sachit")
