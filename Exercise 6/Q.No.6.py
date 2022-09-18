import math

def pizza(d, p):
    up = (1/4 * math.pi*(d/100)**2)/p
    return up
print("for pizza no.1:")
dm = int(input("Enter the diameter in cm: "))
pr = int(input("Enter the prize: "))

print("for pizza no.2: ")
dm2 = int(input("Enter the diameter in cm: "))
pr2 = int(input("Enter the prize:"))

piz = pizza(dm, pr)
piz2 = pizza(dm2, pr2)
print(f'the unit prizes(i.e prize per square meter)of pizza no.1 and pizza no.2 are {piz}euros and {piz2}euros respectively.')
if piz<piz2:
     print(f'pizza no.1 provides better value of prize.')
else:
    print(f'pizza no.2 provides better value of prize.')
