# daily_reminder.py

def main():
    """
    This function prompts the user for a task, its priority, and time sensitivity,
    then provides a customized reminder.
    """

    # --- Step 1: Prompt for a Single Task ---

    # Ask the user for the task description
    task = input("Enter your task description: ")

    # Ask for the task's priority (high, medium, low)
    # Convert input to lowercase to make it case-insensitive for easier matching
    priority = input("Enter task priority (high, medium, low): ").lower()

    # Ask if the task is time-bound (yes or no)
    # Convert input to lowercase for easier checking
    time_bound = input("Is this task time-bound? (yes/no): ").lower()

    # --- Step 2: Process the Task Based on Priority and Time Sensitivity ---

    reminder_message = "" # Initialize an empty string to build our reminder

    # Use a match-case statement to react differently based on priority
    match priority:
        case "high":
            reminder_message = f"Reminder: '{task}' is a HIGH priority task."
        case "medium":
            reminder_message = f"Reminder: '{task}' is a MEDIUM priority task."
        case "low":
            reminder_message = f"Reminder: '{task}' is a LOW priority task."
        case _: # This is the default case if none of the above match
            reminder_message = f"Reminder: '{task}' has an UNKNOWN priority."
            print("Warning: Please enter 'high', 'medium', or 'low' for priority.")

    # Use an if statement to modify the reminder if the task is time-bound
    if time_bound == "yes":
        # Add the time-sensitive phrase to the existing reminder message
        reminder_message += " that requires immediate attention today!"
    elif time_bound != "no": # Handle cases where user enters something other than 'yes' or 'no'
        print("Warning: Please answer 'yes' or 'no' for time-bound.")

    # --- Step 3: Provide a Customized Reminder ---

    print("\n--- Your Daily Reminder ---")
    print(reminder_message)
    print("---------------------------\n")

# This ensures that the main() function runs only when the script is executed directly.
if __name__ == "__main__":
    main()
