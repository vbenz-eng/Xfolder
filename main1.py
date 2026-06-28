
def number_checker(numbers):
    if isinstance(numbers,(int,float)):
        raise ValueError('Invalid input')
    else:
        for index,number in enumerate(numbers, start=1):
            if number % 2 == 1:
                print(f'{index}. {number}, is Odd')
            elif number % 2 == 0:
                print(f'{index}. {number}, is Even')
            else:
                print("invalid input")
num_input = int(input("Enter a number: "))
list = [4, 3, 2, 1]
list.append(num_input)
number_checker(list)