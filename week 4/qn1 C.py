def basic_operations(a, b):
    try:
        addition = a + b
        subtraction = a - b
        multiplication = a * b
        division = a / b
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")
        return None

    results = {
        'addition': addition,
        'subtraction': subtraction,
        'multiplication': multiplication,
        'division': division
    }

    return results


def power_operation(base, exponent, **kwargs):
    try:
        result = base ** exponent
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")
        return None

    if 'modulo' in kwargs:
        modulo = kwargs['modulo']
        try:
            result = result % modulo
        except ZeroDivisionError:
            print("Error: Division by zero is not allowed.")
            return None

    return result


def apply_operations(operation_list):
    results = []
    for operation, args in operation_list:
        try:
            result = operation(*args)
            results.append(result)
        except Exception as e:
            print(f"Error: {e}")
            results.append(None)

    return results

from math_operations import basic_operations, power_operation, apply_operations


result_basic = basic_operations(10, 5)
print("Basic Operations Result:", result_basic)


result_power = power_operation(2, 3)
print("Power Operation Result:", result_power)


result_power_modulo = power_operation(2, 3, modulo=5)
print("Power Operation with Modulo Result:", result_power_modulo)


operations = [
    (lambda x, y: x + y, (3, 4)),
    (lambda x, y: x * y, (2, 5)),
]
result_apply = apply_operations(operations)
print("Apply Operations Result:", result_apply)[2023-12-12 22:43:22] 