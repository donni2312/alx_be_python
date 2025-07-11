# main-0.py
import sys
from bank_account import BankAccount

def main():
    """
    Main function to handle command-line interactions with the BankAccount class.
    """
    # Initialize the account with an example starting balance for demonstration.
    # In a real application, this might be loaded from a persistent storage.
    account = BankAccount(100)

    if len(sys.argv) < 2:
        print("Usage: python main-0.py <command>:<amount>")
        print("Commands:")
        print("  deposit:<amount>   - Deposit money into the account.")
        print("  withdraw:<amount>  - Withdraw money from the account.")
        print("  display            - Display the current account balance.")
        sys.exit(1)

    # Split the command-line argument into command and parameters
    parts = sys.argv[1].split(':')
    command = parts[0]
    
    # Extract amount if present, converting it to a float
    amount = float(parts[1]) if len(parts) > 1 else None

    try:
        if command == "deposit" and amount is not None:
            account.deposit(amount)
        elif command == "withdraw" and amount is not None:
            account.withdraw(amount)
        elif command == "display":
            account.display_balance()
        else:
            print("Invalid command or missing amount for deposit/withdraw.")
            print("Usage: python main-0.py <command>:<amount>")
            print("Commands: deposit, withdraw, display")
            sys.exit(1)
    except ValueError as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()