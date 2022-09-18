import random


def rolldice(max):
    return random.randint(1, max)


i = 0
max = int(input("No of dice roll: "))
while i != max:
    i = rolldice(max)
    print(i)
