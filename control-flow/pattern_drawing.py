# This script draws a square pattern of asterisks based on user-defined size.

def pattern_drawing():
    """
    Prompts the user for a positive integer (size) and then prints
    a square pattern of asterisks of that size using nested loops.
    """
    print("Welcome to the Pattern Drawing Tool!")

    try:
        # Prompt the user to enter the size of the pattern
        size_str = input("Enter the size of the pattern (a positive integer): ")
        size = int(size_str) # Convert the input to an integer

        # Validate that the input is a positive integer
        if size <= 0:
            print("Error: Please enter a positive integer for the pattern size.")
            return # Exit the function if input is not positive

        print(f"\nDrawing a {size}x{size} square pattern:")

        row_count = 0 # Initialize row counter for the while loop

        # Use a while loop to iterate through each row of the pattern
        while row_count < size:
            # Use a for loop to print asterisks for the current row
            for col_count in range(size):
                # Print an asterisk without moving to the next line
                print("*", end="")
            
            # After printing all asterisks for the current row, print a newline
            # to move to the next row
            print()

            row_count += 1 # Increment the row counter

    except ValueError:
        # Handle cases where the user input is not a valid integer
        print("Invalid input. Please enter a whole number.")
    except Exception as e:
        # Handle any other unexpected errors
        print(f"An unexpected error occurred: {e}")

# Call the function to run the script when it's executed
if __name__ == "__main__":
    pattern_drawing()
