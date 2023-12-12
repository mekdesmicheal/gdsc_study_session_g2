def power_operation(base, exponent, **kwargs):
    # Calculate power operation
    result = base ** exponent

    # If 'modulo' is provided in kwargs, calculate modulo
    if 'modulo' in kwargs:
        modulo = kwargs['modulo']
        result = result % modulo

    return result

# Call the power_operation function without modulo
result1 = power_operation(2, 3)
print(result1)  # Output: 8


result2 = power_operation(8, 6, modulo=2)
print(result2)   [2023-12-12 22:43:22] 