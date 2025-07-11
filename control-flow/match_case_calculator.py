# This script implements a simple calculator using a match-case statement.

def match_case_calculator():
    """
    Prompts the user for two numbers and an operation, then performs the
    calculation using a match-case statement and displays the result.
    Handles division by zero.
    """
    print("Welcome to the Match Case Calculator!")

    try:
        # Prompt the user to enter the first number
        num1 = float(input("Enter the first number: "))

        # Prompt the user to enter the second number
        num2 = float(input("Enter the second number: "))

        # Prompt the user to choose an operation
        operation = input("Choose the operation (+, -, *, /): ")

        result = None # Initialize result to None

        # Use a match-case statement to perform the selected operation
        match operation:
            case '+':
                result = num1 + num2
                print(f"The result is {result}")
            case '-':
                result = num1 - num2
                print(f"The result is {result}")
            case '*':
                result = num1 * num2
                print(f"The result is {result}")
            case '/':
                # Handle division by zero case
                if num2 == 0:
                    print("Error: Cannot divide by zero.")
                else:
                    result = num1 / num2
                    print(f"The result is {result}")
            case _:
                # Handle invalid operation input
                print("Invalid operation. Please choose from +, -, *, or /.")

    except ValueError:
        print("Invalid input. Please enter valid numbers.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Call the calculator function to run the script
if __name__ == "__main__":
    match_case_calculator()
