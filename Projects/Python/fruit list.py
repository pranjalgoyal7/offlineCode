# does not works=>
# fruits = ["Mango", "Banana", "watermelon"]

# def li():
#     for i in range(len(fruits) + 1):
#         x = 5
#     for fruit in fruits:
#         print(f"{i}. {fruit}")

# li()
# choice = input('Enter your favourite fruit, you want in list or No : ')
# print(choice)
# if choice == 'No':
#     pass
# else:
#     print('updated list....')
#     fruits.append(choice)
#     li()
#     choice = input('Enter your favourite fruit, you want in list or No : ')
#     print(choice)
print('Welcome to fruit list')
fruits = ["Mango", "Banana", "watermelon"]


def li():
    for i in range(len(fruits)):
        print(f"{i}. {fruits[i]}")


li()
choice = input('Enter your favourite fruit, you want in list or No : ')
print(choice)
for i in range(len(fruits)):
    if choice == 'No':
        pass
    else:
        print('updated list....')
        fruits.append(choice)
        li()
        choice = input('Enter your favourite fruit, you want in list or No : ')
        print(choice)
