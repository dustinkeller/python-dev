def new_sum(num1, num2):
    try:
        raise ValueError("you stupid ")
        return num1/0 + num2
    except (TypeError, ZeroDivisionError) as err:
        print('Please enter numbers: ', err)

print(new_sum(1,'2'))

