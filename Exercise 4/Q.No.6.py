import random


#N = the total no. of random points.
#n = the no. of point that fall inside the circle

N = int(input("enter the no. of point to be generated: "))
n = 0
x = 0

while x < N:
    x += 1
    pX = random.uniform(-1, 1)
    pY = random.uniform(-1, 1)
    if pX ** 2 + pY ** 2 < 1:
        n += 1
piApprox = (4 * n)/N
print(f'the approximate value of pi is {piApprox}.')

