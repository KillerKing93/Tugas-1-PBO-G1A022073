class Calculator:
    def __init__(self):
        pass
    
    def calculate_sum(self, lst):
        return sum(lst)

calc = Calculator()
numbers = [1, 2, 3, 4, 5]
result = calc.calculate_sum(numbers)
print(result)
