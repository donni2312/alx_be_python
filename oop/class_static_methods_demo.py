class Calculator:
    """
    A utility class to demonstrate static and class methods.
    """
    calculation_type = "Arithmetic Operations"

    @staticmethod
    def add(a, b):
        """
        A static method that adds two numbers. It doesn't need access
        to class or instance data, so it's a perfect use case for @staticmethod.
        """
        return a + b

    @classmethod
    def multiply(cls, a, b):
        """
        A class method that multiplies two numbers. It uses the 'cls' parameter
        to access the class-level attribute 'calculation_type'.
        """
        print(f"Calculation type: {cls.calculation_type}")
        return a * b