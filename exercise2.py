import math


def is_number(n):
    try:
        float(n)
        return True
    except ValueError:
        return False


def activation_function():
    x = input("Input x = ")
    if not is_number(x):
        print('x must be a number')
        return

    function_name = input("Input activation Function (sigmoid|relu|elu): ")
    if function_name not in ['sigmoid', 'relu', 'elu']:
        print(f'{function_name} is not supported')
        return

    x = float(x)
    if function_name == 'sigmoid':
        result = 1 / (1 + math.exp(-x))
    elif function_name == 'relu':
        result = max(0, x)
    elif function_name == 'elu':
        alpha = 0.01
        if x <= 0:
            result = alpha * (math.exp(x) - 1)
        else:
            result = x

    print(f'{function_name}: f({x})={result}')

activation_function()