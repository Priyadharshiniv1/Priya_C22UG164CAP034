if 2024 % 4 == 0:
    if 2024 % 100 == 0:
        if 2024 % 400 == 0:
            print("The year is a leap year!")
        else:
            print("The year is not a leap year!")
    else:
        print("The year is a leap year!")
else:
    print("The year is not a leap year!")
