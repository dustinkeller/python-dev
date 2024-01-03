import functools as fn

my_list = [1,2,3,4]


res = fn.reduce(lambda acc, item: acc + item, my_list, 0)
print(res)