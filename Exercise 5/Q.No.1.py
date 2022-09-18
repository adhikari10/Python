import random

rolldice = int(input("enter how many dice to roll: "))
sum = 0
for n in range(1, 6):
    rolldice = random.randint(1, 6)
    sum += rolldice
print(f'sum of rolldice number is {sum}')

