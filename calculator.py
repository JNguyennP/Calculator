def number(num):
    while True:
        try:
            return float(input(num))
        except ValueError:
            print('Error: Value has to be a number')

def get_operator():
    while True:
        op = input('Enter operator (+, -, *, /): ')
        if op in ['+', '-', '*', '/']:
            return op
        else:
            print('Error: Invalid Operator.')      



def performing_calculations(num1, num2, operator):
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        if (num1 != 0 and num2 != 0):
            return num1 / num2
        else:
            print('Error: Dividing by 0 Or Dividing 0 From A Number Is Not Allowed.')




def calculator():
     while True:
        num1 = number('Enter First Number: ')
        operator = get_operator()
        num2 = number('Enter Second Number: ')

        total = performing_calculations(num1, num2, operator)
        print(f'The Total is: {total}')
            
        repeat = input('Do You Want To Perform Another Calculation? Enter Yes or No: ')
        if repeat.lower() != 'yes':
            break



print(calculator())
