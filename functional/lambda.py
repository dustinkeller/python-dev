my_list = [5,4,3]

print(list(map(lambda item: item**2, my_list)))

# List Sorting - sort based on second value
a = [(0,2), (4,3), (9,9), (10,-1)]

a.sort(key=lambda item: item[1])
print(a)