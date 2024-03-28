'''Division function'''

def divide(a, b):
    '''Division'''
    if b == 0:
        raise ValueError("Division by zero is not allowed")
    return a / b
