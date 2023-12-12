def basic_operations(a, b):
    
    addition = a + b
    subtraction = a - b
    multiplication = a * b
    division = a / b

    
    results = {
        'addition': addition,
        'subtraction': subtraction,
        'multiplication': multiplication,
        'division': division
    }

    return results


result = basic_operations(11, 9)

print(result) 


[2023-12-12 22:43:22] 