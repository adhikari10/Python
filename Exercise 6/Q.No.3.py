def quantity(gallon):
    return gallon * 3.785411784

while True:
    gallons = float(input("enter quantity in gallons: "))

    if gallons < 0:
     break
    print(f'{int(gallons)} gallon contain {quantity(gallons)}liters.')



