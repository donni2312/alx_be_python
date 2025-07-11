def display_menu():
    """Displays the menu options for the shopping list manager."""
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    """
    Main function to run the shopping list manager.
    Allows users to add, remove, and view items in their shopping list.
    """
    shopping_list = []  # Initialize an empty list to store shopping items

    while True:
        display_menu()  # Display the menu options
        choice = input("Enter your choice: ")  # Get user's choice

        if choice == '1':
            # Add an item to the list
            item = input("Enter the item to add: ").strip()  # Get item name and remove leading/trailing whitespace
            if item:  # Ensure the item name is not empty
                shopping_list.append(item)  # Add the item to the list
                print(f"'{item}' added to your shopping list. 🛒")
            else:
                print("Item name cannot be empty. Please try again.")

        elif choice == '2':
            # Remove an item from the list
            if not shopping_list:  # Check if the list is empty
                print("Your shopping list is already empty. Nothing to remove.")
                continue

            item_to_remove = input("Enter the item to remove: ").strip()
            if item_to_remove in shopping_list:  # Check if the item exists in the list
                shopping_list.remove(item_to_remove)  # Remove the item
                print(f"'{item_to_remove}' removed from your shopping list.🗑️")
            else:
                print(f"'{item_to_remove}' not found in your shopping list.")

        elif choice == '3':
            # View the current shopping list
            if not shopping_list:  # Check if the list is empty
                print("Your shopping list is empty. Time to add some items! 📝")
            else:
                print("\n--- Your Shopping List ---")
                for i, item in enumerate(shopping_list, 1):  # Iterate and display items with numbers
                    print(f"{i}. {item}")
                print("--------------------------")

        elif choice == '4':
            # Exit the program
            print("Goodbye! Happy shopping! 👋")
            break  # Exit the while loop

        else:
            # Handle invalid menu choices
            print("Invalid choice. Please enter a number between 1 and 4. 🤔")

if __name__ == "__main__":
    main()