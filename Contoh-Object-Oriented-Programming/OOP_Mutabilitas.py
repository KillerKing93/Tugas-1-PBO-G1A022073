class Calculator:
    def __init__(self):
        self.result = 0
    
    def add_numbers(self, num):
        self.result += num

calc = Calculator()
calc.add_numbers(5)
calc.add_numbers(10)
print(calc.result)
