def multiply_by2(li):
    new = []
    for item in li:
        new.append(item*2)
    return new

def mul2(num):
    return num*2

initial = [1,2,3,4,5]
double_list = map(lambda x: x*2,initial)
print(list(double_list))

for item in double_list:
    print('hi')