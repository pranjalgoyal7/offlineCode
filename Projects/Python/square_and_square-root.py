import math
for i in range(10):
    print('Welcome\n1. Calculate a square of number\n2. Calculate square root\n3. Exit')
    a = int(input('Enter your choice : '))
    int(a)
    if a == 3:
        break
    elif a == 1 or a==2:
        if a == 1:
            num = int(input('Enter the number you want to calculate the square of '))
            print(f"The square of {num} is {num * num}\n")
        elif a == 2:
            num = int(input('Enter the number you want to calculate the square root of '))
            print(f"The square root of {num} is {math.sqrt(num)}\n")
    else:
        print('Invalid choice')
# if a == 1:
#     num = int(input('Enter the number you want to calculate the square of '))
#     print(f"The square of {num} is {num * num}")
# elif a == 2:
#     num = int(
#         input('Enter the number you want to calculate the square root of '))
#     print(f"The square root of {num} is {math.sqrt(num)}")
# else:
#     print('Invalid choice')