# bank_account.py

class BankAccount:
    """
    A class to represent a simple bank account.
    Encapsulates account balance and operations like deposit, withdraw, and display.
    """

    def __init__(self, initial_balance=0):
        """
        Initializes a new BankAccount instance.

        Args:
            initial_balance (float, optional): The starting balance for the account. Defaults to 0.
        """
        if not isinstance(initial_balance, (int, float)) or initial_balance < 0:
            raise ValueError("Initial balance must be a non-negative number.")
        self.__account_balance = initial_balance  # Encapsulated attribute

    def deposit(self, amount):
        """
        Deposits a specified amount into the account.

        Args:
            amount (float): The amount to deposit. Must be positive.
        """
        if not isinstance(amount, (int, float)) or amount <= 0:
            raise ValueError("Deposit amount must be a positive number.")
        self.__account_balance += amount
        print(f"Deposited: ${amount}")

    def withdraw(self, amount):
        """
        Withdraws a specified amount from the account if sufficient funds are available.

        Args:
            amount (float): The amount to withdraw. Must be positive.

        Returns:
            bool: True if the withdrawal was successful, False otherwise (insufficient funds).
        """
        if not isinstance(amount, (int, float)) or amount <= 0:
            raise ValueError("Withdrawal amount must be a positive number.")
        if self.__account_balance >= amount:
            self.__account_balance -= amount
            print(f"Withdrew: ${amount}")
            return True
        else:
            print("Insufficient funds.")
            return False

    def display_balance(self):
        """
        Displays the current account balance in a user-friendly format.
        """
        print(f"Current Balance: ${self.__account_balance}")