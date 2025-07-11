# This script generates a multiplication table for a user-provided number.

def multiplication_table():
    """
    Prompts the user for a number and then prints its multiplication table
    from 1 to 10 using a for loop.
    """
    print("Welcome to the Multiplication Table Generator!")

    try:
        # Prompt the user to enter a number
        number_str = input("Enter a number to see its multiplication table: ")
        number = int(number_str) # Convert the input to an integer

        print(f"\nMultiplication Table for {number}:")
        # Use a for loop to iterate from 1 to 10
        for i in range(1, 11): # range(1, 11) includes 1 and goes up to (but not including) 11
            product = number * i # Calculate the product
            # Print each line of the multiplication table in the specified format
            print(f"{number} * {i} = {product}")

    except ValueError:
        # Handle cases where the user input is not a valid integer
        print("Invalid input. Please enter a whole number.")
    except Exception as e:
        # Handle any other unexpected errors
        print(f"An unexpected error occurred: {e}")

# Call the function to run the script when it's executed
if __name__ == "__main__":
    multiplication_table()
