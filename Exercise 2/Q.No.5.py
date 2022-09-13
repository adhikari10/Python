talents = int(input("enter talents:"))
pounds = int(input("enter pounds:"))
lots = float(input("enter lots:"))
Sum = (talents*20*32*13.3 + pounds*32*13.3 + lots*13.3)
kilogram = Sum/1000
gram = (kilogram-int(kilogram))*1000
print("the weight in modern units:")
print(f'{int(kilogram)} kilogram and {gram:.2f} grams')


















