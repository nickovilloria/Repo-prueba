def logging_decorator(func):
    def wrapper(*args, **kwargs):
        print(f"Calling function: {func.__name__}")
        print(f"Arguments: {args}, {kwargs}")
        result = func(*args, **kwargs)
        print(f"Function {func.__name__} returned: {result}")
        return result
    return wrapper

a=input("Ingrese primer número: ")
b=input("Ingrese segundo número: ")
@logging_decorator
def add(a, b):
    return a + b

# Example usage
add(int(a), int(b))
