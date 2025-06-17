def has_duplicates(arr):
    counts = {}  # Dictionary to store counts of each number

    for num in arr:
        if num in counts:
            counts[num] += 1  # Increment count if number is already in the dictionary
        else:
            counts[num] = 1  # Initialize count if number is not in the dictionary

    # Filter out numbers that are not repeated
    repeated = {num: count for num, count in counts.items() if count > 1}
    
    return repeated

# Get input and convert it to a list of integers
arr = list(map(int, input('Provide a list of integers separated by commas: ').split(',')))
result = has_duplicates(arr)
print(result)