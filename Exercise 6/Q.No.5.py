def integer(list):
    for x in list:
        if x % 2 != 0:
            list.remove(x)


list1 = [2, 5, 67, 300, 891, 1000]
print(list1)
integer(list1)
print(list1)


