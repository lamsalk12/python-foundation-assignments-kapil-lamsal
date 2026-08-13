# Define the raw list containing a mix of valid ints, None, and invalid strings
raw_values = [100, None, 250, "invalid", 300, None, 450]

# --- Approach 1: loop + continue + isinstance() ---

# Create an empty list to collect valid integers
clean_values_loop = []

# Loop through every value in the raw list
for value in raw_values:
    # Skip this value if it is NOT an integer
    # (isinstance check also guards against True/False, which are technically
    # ints in Python, but that's not a concern with this dataset)
    if not isinstance(value, int):
        # Skip to the next item without adding this one
        continue

    # If we reach this line, the value is a valid integer, so add it
    clean_values_loop.append(value)

# Print the result from the loop-based approach
print("Loop approach:", clean_values_loop)

# --- Approach 2: list comprehension ---

# Build the same result in a single line using a list comprehension
clean_values_comprehension = [value for value in raw_values if isinstance(value, int)]

# Print the result from the list comprehension approach
print("Comprehension approach:", clean_values_comprehension)
