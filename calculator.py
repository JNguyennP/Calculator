def calculator():
    while True:
        try: 
            num1 = float(input('Enter First Number: '))

            operator = input('Enter operator (+, -, *, /):')

            num2 = float(input('Enter Second Number: '))

            # if operator == '+':
            #     total = num1 + num2
            # elif operator == '-':
            #     total = num1 - num2
            # elif operator == '*':
            #     total = num1 * num2
            # elif operator == '/':
            #     if (num1 != 0 and num2 != 0):
            #         total - num1 / num2
            #     else:
            #         print('Error: Dividing by 0 Or Dividing 0 From A Number Is Not Allowed.')
            # else: 
            #     print('Invalid Operator.')

            # print(f'The result is: {total}')
        
        except ValueError:
            print('Error: Invalid Input. Please Enter A Number.')
        
        repeat = input('Do You Want To Perform Another Calculation? Enter Yes or No: ')
        if repeat.lower() != 'yes':
            break

def number(num):
    while True:
        try:
            return float(input(num))
        except ValueError:
            print('Error: Value has to be a number')

def operator(op):
    while True:
        op = input('Enter operator (+, -, *, /): ')
        if operator in ['+', '-', '*', '/']:
            return op
        else:
            print('Error: Invalid Operator.')      



def performing_calculations(num1, num2, operator):
    if operator == '+':
        total = num1 + num2
    elif operator == '-':
        total = num1 - num2
    elif operator == '*':
        total = num1 * num2
    elif operator == '/':
        if (num1 != 0 and num2 != 0):
            total - num1 / num2
        else:
            print('Error: Dividing by 0 Or Dividing 0 From A Number Is Not Allowed.')
    else: 
        print('Invalid Operator.')

    print(f'The result is: {total}')





print(calculator())
