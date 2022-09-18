def sum_of_numbers(list):
    sum=0
    for x in list:
        sum += x
    return sum


lists = [1, 20, 200, 855, 25990]
sum = sum_of_numbers(lists)
print(sum)