# daily_reminder.py

def main():
    """
    This function prompts the user for a task, its priority, and time sensitivity,
    then provides a customized reminder.
    """

   
    task = input("Enter your task:")

    
    priority = input("Priority (high/medium/low):").lower()

   
    time_bound = input("Is it time-bound? (yes/no):").lower()

   
    print("Reminder")

    
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

    

    print("Reminder")
    print(reminder_message)
    print("---------------------------\n")

# This ensures that the main() function runs only when the script is executed directly.
if __name__ == "__main__":
    main()
