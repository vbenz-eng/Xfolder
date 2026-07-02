

numbers = [int(input("Enter number: "))]

for number in numbers:
    if  isinstance(number, (int,float)):
        if number % 2 == 1:
            print(f'{number}, is Odd')
        elif number % 2 == 0:
            print(f'{number}, is Even')
        else:
            print("invalid input")
    else:
        print("invalid input")complete
        
print("Program completed")
