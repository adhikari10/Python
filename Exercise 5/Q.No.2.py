print("enter an empty string if you want to exit. ")
x = 1
num_l = []

while x > 0:
    num = (input("Enter a number: "))

    if num == "":
        break
    else:
        num_l.append(int(num))

num_l.sort(reverse=True)
print(num_l)
print(f'The five greatest number are {num_l[0:5]}.')






