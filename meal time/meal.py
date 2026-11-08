def main():
    time, half_day = input("What time is it? ").split(" ")
    time = convert(time)
    if half_day:
        if (half_day == "a.m.") and (7.00 <= time <= 8.00):
            print("breakfast time")
        elif (half_day == "p.m.") and (0.00 <= time <= 1.00):
             print("lunch time")
        elif (half_day == "p.m.") and (6.00 <= time <= 7.00):
             print("dinner time")
#    if 7.00 <= time <= 8.00:
#        print("breakfast time")
#    elif 12.00 <= time <= 13.00:
#        print("lunch time")
#    elif 18.00 <= time <= 19.00:
#        print("dinner time")


def convert(time:str):
    hours, minutes = time.split(":")
    if hours == 12.00:
        hours = 0.0
    return float(hours) + float(minutes)/60.


if __name__ == "__main__":
    main()