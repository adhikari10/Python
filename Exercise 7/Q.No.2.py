name_set = set()
while True:
    name = input("Enter a name:")
    if name == "":
        break

    if name in name_set:
        print("Already existed")
    else:
        print("New name")
    name_set.add(name)


for i in name_set:
    print(i)


