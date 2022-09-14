cabinClass = input("enter your cabinclass: ")
cabinClass = cabinClass.lower()
if cabinClass == "lux":
    print("Lux on a balcony cabin of upper deck.")
elif cabinClass == "a":
    print("A on the window cabin above the car deck.")
elif cabinClass == "b":
    print("B om a windowless cabin above the car deck.")
elif cabinClass == "c":
    print("c on the windowless cabin below the car deck.")
else:
    print("Invalid cabin class")

