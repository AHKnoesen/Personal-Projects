import math

def basic_operation(operator, x, y):
    if operator == '+':
        return x + y
    elif operator == '-':
        return x - y
    elif operator == '*':
        return x * y
    elif operator == '/':
        return x / y
    elif operator == '**':
        return x ** y

def scientific_operation(operator, x):
    if operator == 'sin':
        return math.sin(x)
    elif operator == 'cos':
        return math.cos(x)
    elif operator == 'tan':
        return math.tan(x)
    elif operator == 'log':
        return math.log10(x)
    elif operator == 'ln':
        return math.log(x)


print('Available operations:')
print('  +   -   *   /   **')
print('  sin cos tan log ln')

while True:
    user_input = input('Enter an expression (q to quit): ')

    if user_input == 'q':
        break

    
    operator, *operands = user_input.split()

    operands = [float(x) for x in operands]

    if operator in ['+', '-', '*', '/', '**']:
        result = basic_operation(operator, *operands)
    elif operator in ['sin', 'cos', 'tan', 'log', 'ln']:
        result = scientific_operation(operator, *operands)
    else:
        print('Invalid operator')
        continue

    print('Result:', result)
