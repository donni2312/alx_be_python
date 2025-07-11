from polymorphism_demo import Shape, Rectangle, Circle
import math

def main():
    # Create a list of different shape objects
    shapes = [
        Rectangle(10, 5),
        Circle(7)
    ]

    # Demonstrate polymorphism by calling the same method on different objects
    for shape in shapes:
        # The correct area() method is called based on the object's type
        print(f"The area of the {shape.__class__.__name__} is: {shape.area()}")

if __name__ == "__main__":
    main()