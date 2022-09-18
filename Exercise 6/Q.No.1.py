import random


def rolldice():
    return random.randint(1, 6)


i = 0
while i != 6:
    i = rolldice()
    print(i)
