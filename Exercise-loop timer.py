import time

# time.sleep(3) #Sleep for amout of time
vr = input("What is the timer for?(D/H/M/S): ")
d = "D"
h = "H"
m = "M"
s = "S"
if vr == d:
    dayss = int(input("Enter the time in days: "))
    my_time = dayss * 24 * 60 * 60

    for x in range(my_time, 0, -1):
        seconds = x % 60
        minutes = int(x / 60) % 60
        hours = int(x / 3600) % 24
        days = int(x / 86400) % 24
        print(f"Remaining: {days:02}:{hours:02}:{minutes:02}:{seconds:02}")
        time.sleep(1)
elif vr == h:
    hourss = int(input("Enter the time in hours: "))
    my_time = hourss * 60 * 60

    for x in range(my_time, 0, -1):
        seconds = x % 60
        minutes = int(x / 60) % 60
        hours = int(x / 3600) % 24
        days = int(x / 86400) % 24
        print(f"Remaining: {days:02}:{hours:02}:{minutes:02}:{seconds:02}")
        time.sleep(1)
elif vr == m:
    minutess = int(input("Enter the time in minutes: "))
    my_time = minutess * 60

    for x in range(my_time, 0, -1):
        seconds = x % 60
        minutes = int(x / 60) % 60
        hours = int(x / 3600) % 24
        days = int(x / 86400) % 24
        print(f"Remaining: {days:02}:{hours:02}:{minutes:02}:{seconds:02}")
        time.sleep(1)
elif vr == s:
    secondss = int(input("Enter the time in seconds: "))
    my_time = secondss

    for x in range(my_time, 0, -1):
        seconds = x % 60
        minutes = int(x / 60) % 60
        hours = int(x / 3600) % 24
        days = int(x / 86400) % 24
        print(f"Remaining: {days:02}:{hours:02}:{minutes:02}:{seconds:02}")
        time.sleep(1)
else:
    print("Invalid input.Try again!")
print("TIME'S UP!")
input("\n\nThe end!")