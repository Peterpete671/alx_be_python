class Calculator:
    """A simple calculator class demonstrating static and class methods."""

    # Class attribute
    calculation_type = "Arithmetic Operations"

    @staticmethod
    def add(a, b):
        """Static method that returns the sum of two numbers."""
        return a + b

    @classmethod
    def multiply(cls, a, b):
        """Class method that prints calculation type and returns the product."""
        print(f"Calculation type: {cls.calculation_type}")
        return a * b
