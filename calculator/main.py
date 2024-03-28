'''file to start calculator prompts'''

from calculator import Calculator

calculator = Calculator()

def display_history():
    '''display history function'''
    print("Calculation History:")
    for i, (expression, result) in enumerate(calculator.get_history(), start=1):
        print(f"{i}. {expression} = {result}")

if __name__ == "__main__":
    while True:
        choice = input("Enter choice (add, subtract, multiply, divide,"
                       "show history, clear history, exit): ")
        if choice == 'show history':
            display_history()
        elif choice == 'clear history':
            calculator.clear_history()
            print("History cleared.")
        elif choice == 'exit':
            break

        elif choice in ['add', 'subtract', 'multiply', 'divide']:
            num1 = input("Enter first number: ")
            num2 = input("Enter second number: ")

            try:
                num1 = float(num1)
                num2 = float(num2)
            except ValueError:
                print("Invalid input. Please enter numeric values.")
                continue

            if choice == 'add':
                result = calculator.add(num1, num2)
                print("Result:", result)
            elif choice == 'subtract':
                result = calculator.subtract(num1, num2)
                print("Result:", result)
            elif choice == 'multiply':
                result = calculator.multiply(num1, num2)
                print("Result:", result)
            elif choice == 'divide':
                try:
                    result = calculator.divide(num1, num2)
                    print("Result:", result)
                except ValueError as e:
                    print("Error:", e)
        else:
            print("Invalid choice")
