'''file to start calculator prompts'''
from add import add
from subtract import subtract
from multiply import multiply
from divide import divide

if __name__ == "__main__":
    # Example usage
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    print("Addition")
    print("Subtraction")
    print("Multiplication")
    print("Division")
    choice = input("Enter choice (addition, subtraction, multiplication, division): ")

    if choice == 'addition':
        print("Result:", add(num1, num2))
    elif choice == 'subtraction':
        print("Result:", subtract(num1, num2))
    elif choice == 'multiplication':
        print("Result:", multiply(num1, num2))
    elif choice == 'division':
        try:
            print("Result:", divide(num1, num2))
        except ValueError as e:
            print("Error:", e)
    else:
        print("Invalid choice")
