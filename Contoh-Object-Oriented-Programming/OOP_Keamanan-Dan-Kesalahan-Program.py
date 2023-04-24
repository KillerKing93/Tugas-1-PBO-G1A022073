class Calculator:
    def __init__(self):
        self.result = 0
    
    def add_numbers(self, num):
        self.result += num
    
    def subtract_numbers(self, num):
        self.result -= num

calc = Calculator()
calc.add_numbers(10)
calc.subtract_numbers(5)
print(calc.result)
