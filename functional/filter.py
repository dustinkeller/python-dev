def odd(num):
    return num % 2 != 0

L = [1,2,3,4,5,6,7,8]
filtered = filter(odd, L)
# print(list(filtered))

for item in filtered:
    print(item * 2)