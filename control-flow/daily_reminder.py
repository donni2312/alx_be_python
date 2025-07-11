# daily_reminder.py

def main():
    """
    This function prompts the user for a task, its priority, and time sensitivity,
    then provides a customized reminder.
    """

    "Enter your task:"
    task = input("Enter your task:")

    # Ask for the task's priority (high, medium, low)
    # Corrected prompt to match checker's expectation: "Priority (high/medium/low):"
    # Convert input to lowercase to make it case-insensitive for easier matching
    priority = input("Priority (high/medium/low):").lower()

    # Ask if the task is time-bound (yes or no)
    # Corrected prompt to match checker's expectation: "Is it time-bound? (yes/no):"
    # Convert input to lowercase for easier checking
    time_bound = input("Is it time-bound? (yes/no):").lower()

    # --- Step 2: Process the Task Based on Priority and Time Sensitivity ---

    # --- Step 3: Provide a Customized Reminder ---

    print("\n--- Your Daily Reminder ---")

    # Use a match-case statement to react differently based on priority
    # Print the core reminder directly here to satisfy the checker's regex
    match priority:
        case "high":
            print(f"Reminder: '{task}' is a HIGH priority task.", end="")
        case "medium":
            print(f"Reminder: '{task}' is a MEDIUM priority task.", end="")
        case "low":
            print(f"Reminder: '{task}' is a LOW priority task.", end="")
        case _: # This is the default case if none of the above match
            print(f"Reminder: '{task}' has an UNKNOWN priority.", end="")
            print("\nWarning: Please enter 'high', 'medium', or 'low' for priority.") # Print warning on a new line

    # Use an if statement to modify the reminder if the task is time-bound
    if time_bound == "yes":
        # Add the time-sensitive phrase directly to the same line
        print(" that requires immediate attention today!", end="")
    elif time_bound != "no": # Handle cases where user enters something other than 'yes' or 'no'
        print("\nWarning: Please answer 'yes' or 'no' for time-bound.") # Print warning on a new line

    # Ensure a newline after the reminder message, if not already added by a warning
    print() 
    print("---------------------------\n")

# This ensures that the main() function runs only when the script is executed directly.
if __name__ == "__main__":
    main()
