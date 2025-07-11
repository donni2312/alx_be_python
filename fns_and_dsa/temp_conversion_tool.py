# temp_conversion_tool.py

# Define Global Conversion Factors
# These factors are accessible throughout the script.
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5
CELSIUS_OFFSET = 32 # The offset used in both conversion formulas

def convert_to_celsius(fahrenheit):
    """
    Converts a temperature from Fahrenheit to Celsius.

    Args:
        fahrenheit (float): The temperature in Fahrenheit.

    Returns:
        float: The temperature converted to Celsius.
    """
    # Formula: (F - 32) * (5/9)
    celsius = (fahrenheit - CELSIUS_OFFSET) * FAHRENHEIT_TO_CELSIUS_FACTOR
    return celsius

def convert_to_fahrenheit(celsius):
    """
    Converts a temperature from Celsius to Fahrenheit.

    Args:
        celsius (float): The temperature in Celsius.

    Returns:
        float: The temperature converted to Fahrenheit.
    """
    # Formula: (C * 9/5) + 32
    fahrenheit = (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + CELSIUS_OFFSET
    return fahrenheit

def main():
    """
    Main function to run the temperature conversion tool.
    Prompts the user for temperature and unit, then performs and displays the conversion.
    """
    print("--- Temperature Conversion Tool ---")

    while True:
        try:
            # Get temperature input from the user
            temp_input = input("Enter the temperature value (e.g., 25): ").strip()
            temperature = float(temp_input) # Attempt to convert to float

            # Get unit input from the user
            unit_input = input("Enter the unit (C for Celsius, F for Fahrenheit): ").strip().upper()

            if unit_input == 'C':
                # Convert Celsius to Fahrenheit
                converted_temp = convert_to_fahrenheit(temperature)
                print(f"{temperature}°C is equal to {converted_temp:.2f}°F")
            elif unit_input == 'F':
                # Convert Fahrenheit to Celsius
                converted_temp = convert_to_celsius(temperature)
                print(f"{temperature}°F is equal to {converted_temp:.2f}°C")
            else:
                # Handle invalid unit input
                print("Invalid unit. Please enter 'C' or 'F'.")
                continue # Continue the loop to ask for input again

            # Ask if the user wants to perform another conversion
            another_conversion = input("Do you want to convert another temperature? (yes/no): ").strip().lower()
            if another_conversion != 'yes':
                print("Thank you for using the Temperature Conversion Tool! Goodbye! 👋")
                break # Exit the loop if user doesn't want to convert again

        except ValueError:
            # Catch ValueError if temperature input is not numeric
            print("Invalid temperature. Please enter a numeric value.")
        except Exception as e:
            # Catch any other unexpected errors
            print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()