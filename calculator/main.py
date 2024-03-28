'''file to start calculator prompts'''

from calculator import Calculator

calculator = Calculator()

if __name__ == "__main__":
    while True:

        choice = input("Enter choice (add, subtract, multiply, divide, "
                       "show history, clear history, exit): ")

        if choice == 'show history':
            for i, (expression, result) in enumerate(calculator.get_history(), start=1):
                print(f"{i}. {expression} = {result}")
        elif choice == 'clear history':
            calculator.clear_history()
            print("History cleared.")
        elif choice == 'exit':
            break
        elif choice in ['add', 'subtract', 'multiply', 'divide']:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            try:
                result = calculator.perform_operation(choice, num1, num2)
                print("Result:", result)
            except ValueError as e:
                print("Error:", e)
        else:
            print("Invalid choice")
