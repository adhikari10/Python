import sys

print("enter a empty string if you want to exit.")
x = 1
num1 = []
while x > 0:
    num = input("enter a number: ")
    if num == "":
        break
    else:
        num1.append(num)

largest = max(num1)
smallest = min(num1)

print(f'the largest number is {largest} and smallest number is {smallest} ')
