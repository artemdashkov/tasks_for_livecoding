def factorial_function(x: int) -> int:
    result = 1
    for x in range(1, x+1):
        result *= x
    return result

print(factorial_function(6))