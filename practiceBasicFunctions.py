"""For practicing Catching errors"""

# Function with two parameters


def add_nums(num1, num2):
    """Testing for functions"""
    sumar = num1 + num2
    return sumar


# Call function using parameters
RESULT = add_nums(5, 3)
"""Testing for functions"""
print(RESULT)

# Function with default parameter


def hello(name="John"):
    """Testing for functions"""
    print("Hello " + name)


hello()  # Uses default name
# hello("Jane")  # Overrides default

# Function with code block


def print_lines():
    """Testing for printing"""
    print("Line 1")
    print("Line 2")
    print("Line 3")


print_lines()
