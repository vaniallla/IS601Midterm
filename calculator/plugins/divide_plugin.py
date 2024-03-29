'''Division class'''
# pylint: disable=too-few-public-methods

class DividePlugin:
    '''Division Class'''
    def execute(self, a, b):
        '''Division function'''
        if b == 0:
            raise ValueError("Division by zero is not allowed")
        return a / b
