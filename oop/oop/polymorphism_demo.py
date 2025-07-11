import math

class Shape:
    """A base class for geometric shapes that defines an interface for area calculation."""
    def area(self):
        """
        Calculates the area of the shape. This method is meant to be overridden
        by derived classes.
        """
        raise NotImplementedError("Subclasses must implement the area() method.")

class Rectangle(Shape):
    """A rectangle shape, inheriting from Shape."""
    def __init__(self, length: float, width: float):
        """Initializes the rectangle with length and width."""
        self.length = length
        self.width = width

    def area(self) -> float:
        """Overrides the base method to calculate the area of the rectangle."""
        return self.length * self.width

class Circle(Shape):
    """A circle shape, inheriting from Shape."""
    def __init__(self, radius: float):
        """Initializes the circle with a radius."""
        self.radius = radius

    def area(self) -> float:
        """Overrides the base method to calculate the area of the circle."""
        return math.pi * (self.radius ** 2)