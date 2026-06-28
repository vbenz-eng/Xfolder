
def number_checker(numbers):
    if isinstance(numbers,(int,float)):
        numbers = [numbers]

    for index,number in enumerate(numbers, start=1):
        if number % 2 == 1:
            print(f'{index}. {number}, is Odd')
        elif number % 2 == 0:
            print(f'{index}. {number}, is Even')
        else:
            print("invalid input")
num_input = input("Enter comma separated numbers: ")
saved_numbers = [int(x.strip()) for x in num_input.split(',')]

number_checker(saved_numbers)