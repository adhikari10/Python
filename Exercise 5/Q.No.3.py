number = int(input("enter an integer: " ))
primeNumber = True
for x in range(2, number):
    if number%x == 0:
        primeNumber = False
        break

if primeNumber:
    print(f'{number} is prime number.')
else:
    print(f'{number} is not a prime Number')



