import random

threedigitcodes = ""

fourdigitcodes = ""

for x in range(3):
    threedigitcodes += str(random.randint(0, 9))
for x in range(4):
    fourdigitcodes += str(random.randint(1, 6))
print(" Three digit codes:" +threedigitcodes)
print(" Four digit codes:" +fourdigitcodes)



