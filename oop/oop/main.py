from class_static_methods_demo import Calculator

def main():
    """
    Tests the Calculator class's static and class methods.
    """
    # Using the static method - called directly on the class
    sum_result = Calculator.add(10, 5)
    print(f"The sum is: {sum_result}")

    # Using the class method - also called directly on the class
    product_result = Calculator.multiply(10, 5)
    print(f"The product is: {product_result}")

if __name__ == "__main__":
    main()