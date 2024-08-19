def calculator():
    num1 = float(input('Enter First Number: '))

    operator = input('Enter operator (+, -, *, /):')

    num2 = float(input('Enter Second Number: '))

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
            return 'Error: Dividing by 0 Or Dividing 0 From A Number Is Not Allowed.'
    else: 
        return 'Invalid Operator.'

    return f'The result is: {total}'

print(calculator())
