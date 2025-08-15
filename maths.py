import math

def basic_operation(operator, x, y):
    if operator == '+':
        return x + y
    elif operator == '-':
        return x - y
    elif operator == '*':
        return x * y
    elif operator == '/':
        if y == 0:
            raise ValueError("Cannot divide by zero")
        return x / y
    elif operator == '**':
        try:
            return x ** y
        except OverflowError:
            raise ValueError("Result too large to compute")

def scientific_operation(operator, x):
    if operator == 'sin':
        return math.sin(x)
    elif operator == 'cos':
        return math.cos(x)
    elif operator == 'tan':
        return math.tan(x)
    elif operator == 'log':
        if x <= 0:
            raise ValueError("Logarithm undefined for non-positive numbers")
        return math.log10(x)
    elif operator == 'ln':
        if x <= 0:
            raise ValueError("Natural logarithm undefined for non-positive numbers")
        return math.log(x)


print('Available operations:')
print('  +   -   *   /   **')
print('  sin cos tan log ln')

while True:
    user_input = input('Enter an expression (q to quit): ')

    if user_input == 'q':
        break

    try:
        parts = user_input.split()
        if len(parts) == 0:
            print('Please enter an expression')
            continue
            
        operator = parts[0]
        operands_str = parts[1:]
        
        # Convert operands to float with error handling
        try:
            operands = [float(x) for x in operands_str]
        except ValueError as e:
            print(f'Invalid number format: {e}')
            continue

        if operator in ['+', '-', '*', '/', '**']:
            if len(operands) != 2:
                print(f'Operator "{operator}" requires exactly 2 operands, got {len(operands)}')
                continue
            result = basic_operation(operator, *operands)
        elif operator in ['sin', 'cos', 'tan', 'log', 'ln']:
            if len(operands) != 1:
                print(f'Operator "{operator}" requires exactly 1 operand, got {len(operands)}')
                continue
            result = scientific_operation(operator, *operands)
        else:
            print(f'Invalid operator: {operator}')
            continue

        print('Result:', result)
        
    except ValueError as e:
        print(f'Error: {e}')
    except Exception as e:
        print(f'Unexpected error: {e}')
