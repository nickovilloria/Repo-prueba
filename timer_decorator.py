import time

def timer_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()  # Record the start time
        result = func(*args, **kwargs)  # Call the original function
        end_time = time.time()  # Record the end time
        execution_time = end_time - start_time  # Calculate the execution time
        print(f"Execution time: {execution_time:.20f} seconds")  # Print the execution time
        return result  # Return the result of the original function
    return wrapper

@timer_decorator
def example_function(n):
    total = 0
    for i in range(n):
        total += i
    return total

# Call the decorated function
result = example_function(1000000)
print(f"Result: {result}")