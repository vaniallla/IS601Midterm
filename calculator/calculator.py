'''calculator file'''
# from add import add
# from subtract import subtract
# from multiply import multiply
# from divide import divide

class Calculator:
    '''calculator class to store history'''
    def __init__(self):
        self.history = []

    def add_to_history(self, expression, result):
        '''function to add calculation to history'''
        self.history.append((expression, result))

    def get_history(self):
        '''function to retrieve history'''
        return self.history

    def clear_history(self):
        '''function to clear history'''
        self.history = []

    def add(self, a, b):
        '''addition function'''
        result = a + b
        self.add_to_history(f"{a} + {b} = {result}", result)
        return result

    def subtract(self, a, b):
        '''subtraction function'''
        result = a - b
        self.add_to_history(f"{a} - {b} = {result}", result)
        return result

    def multiply(self, a, b):
        '''multiply function'''
        result = a * b
        self.add_to_history(f"{a} * {b} = {result}", result)
        return result

    def divide(self, a, b):
        '''division function'''
        if b == 0:
            raise ValueError("Division by zero is not allowed")
        result = a / b
        self.add_to_history(f"{a} / {b} = {result}", result)
        return result
