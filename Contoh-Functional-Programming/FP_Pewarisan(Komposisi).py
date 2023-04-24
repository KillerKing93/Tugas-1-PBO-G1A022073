def add(x, y):
    return x + y

def multiply(x, y):
    return x * y

def calculate(a, b, c):
    return multiply(add(a, b), c)

result = calculate(2, 3, 4)
print(result)
