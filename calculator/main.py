'''file to start calculator prompts'''

from calculator import Calculator

calculator = Calculator()

if __name__ == "__main__":
    while True:

        choice = input("Enter choice (add, subtract, multiply, divide, "
                       "show history, clear history, save history, load history, "
                       "delete history, exit): ")

        if choice == 'show history':
            print("History:")
            history_df = calculator.get_history()
            for i, row in history_df.iterrows():
                expression = row['Expression']
                result = row['Result']
                print(f"{i}. {expression} = {result}")
        elif choice == 'clear history':
            calculator.clear_history()
            print("History cleared.")
        elif choice == 'save history':
            filename = input("Enter filename to save history: ")
            calculator.save_history(filename)
            print(f"History saved to {filename}")
        elif choice == 'load history':
            filename = input("Enter filename to load history from: ")
            calculator.load_history(filename)
            print(f"History loaded from {filename}")
        elif choice == 'delete history':
            filename = input("Enter filename to delete history: ")
            calculator.delete_file(filename)
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
