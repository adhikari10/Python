def airport(fetch,store):
    for i in fetch:
        if i == store:
            return True
        return False

airports = {}
while True:
    print("\n")
    print("Do you want to add, search oe exit for airports? (add, search, x)")
    command = input("Input: ")

    #Add airport
    if command == "add":
        icoa = input("Enter ICOA code: ")
        if airport(airports, icoa):
            print("(Warning: The key is already in use!)")
            if input("Save new? (y/n): ") != "y":
                continue

        name = input("Enter the name of the airport: ")
        airports.update({icoa: name})
        print("Airport added")

    #Search for an airport
    elif command == "search":
        icoa = input("Enter ICOA code: ")
        if airport(airports, icoa):
            print(f"Icoa code: {icoa} matches airport: {airports.get(icoa)}")
        else:
            print("No airport found")

    #Exit the program
    elif command == "x":
        print("Exiting the program...")
        break

    #Error
    else:
        print("Wrong command")