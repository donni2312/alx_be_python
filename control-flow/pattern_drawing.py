# pattern_drawing.py

# This script draws a square pattern of asterisks based on user-defined size.

def pattern_drawing():
    """
    Prompts the user for a positive integer (size) and then prints
    a square pattern of asterisks of that size using nested loops.
    """
    print("Welcome to the Pattern Drawing Tool!")

    try:
        size = int(input("Enter the size of the pattern:"))

        if size <= 0:
            print("Error: Please enter a positive integer for the pattern size.")
            return # Exit the function if input is not positive

        print(f"\nDrawing a {size}x{size} square pattern:")

        row_count = 0 # Initialize row counter for the while loop

        while row_count < size:
            # Inner loop to print asterisks for each column in the current row
            for col_count in range(size):
                # print("*", end="") keeps the print cursor on the same line
                print("*", end="")
            
            # After printing all asterisks for a row, move to the next line
            print()

            row_count += 1 # Increment the row counter to move to the next row

    except ValueError:
        # Handle cases where the user enters non-integer input
        print("Invalid input. Please enter a whole number.")
    except Exception as e:
        # Catch any other unexpected errors
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    pattern_drawing()

