while True:
    value = float(input("Enter a positive number in inches: "))
    if value < 0:
        break

    else:
        centimeterValue = value * 2.54
        print(f"{value} inches is {centimeterValue:0.2f} centimeter")




