# Error Handling
while True:
    try:
        age = int(input('What is your age? '))
        print(f"On your birthday you will be {age+1} years old!")
        print(f"For fun, 10 divided by your age is {10/age}")
        break
    except(ValueError):
        print('please enter a number...')
    except(ZeroDivisionError):
        print('please enter a nonzero age...')
    