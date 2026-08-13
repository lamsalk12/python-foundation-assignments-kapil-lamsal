# Loop through batch numbers 1 to 10 (inclusive) using range()
for batch_number in range(1, 11):
    # Print the current batch being processed
    print(f"Processing batch {batch_number}")

    # Check if the current batch number is a multiple of 3
    if batch_number % 3 == 0:
        # Display a checkpoint message after every third batch
        print("Checkpoint reached")
