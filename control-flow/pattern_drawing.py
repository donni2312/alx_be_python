# This script draws a square pattern of asterisks based on user-defined size.

def pattern_drawing():
    """
    Prompts the user for a positive integer (size) and then prints
    a square pattern of asterisks of that size using nested loops.
    """
    print("Welcome to the Pattern Drawing Tool!")

    try:
        size_str = input("Enter the size of the pattern (a positive integer): ")
        size = int(size_str) # Convert the input to an integer

        
        if size <= 0:
            print("Error: Please enter a positive integer for the pattern size.")
            return # Exit the function if input is not positive

        print(f"\nDrawing a {size}x{size} square pattern:")

        row_count = 0 # Initialize row counter for the while loop

       
        while row_count < size:
           
            for col_count in range(size):
                
                print("*", end="")
            
            
            print()

            row_count += 1 # Increment the row counter

    except ValueError:
       
        print("Invalid input. Please enter a whole number.")
    except Exception as e:
        
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    pattern_drawing()
