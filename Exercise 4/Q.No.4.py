import random

num = random.randint(1, 10)
guess = 0
print(" Number between 1 to 10 ! ")
while guess != num:
    guess = float(input("guess a number: "))
    if guess > num:
        print("too high")
    if guess < num:
        print("too low")
print("correct")
