# Track the current attempt number, starting at 1
attempt = 1

# Define the maximum number of retry attempts allowed
max_attempts = 3

# Track whether the operation has succeeded yet
operation_successful = False

# Stretch: simulate the operation succeeding on the 2nd attempt.
# Set this to None to always fail (base exercise behavior),
# or to a number (e.g. 2) to simulate success on that attempt.
succeed_on_attempt = 2

# Keep looping while we haven't exceeded max attempts
while attempt <= max_attempts:
    # Print which attempt is currently running
    print(f"Attempt {attempt}")

    # Simulate success if this attempt matches the "succeed_on_attempt" setting
    if succeed_on_attempt is not None and attempt == succeed_on_attempt:
        # Mark the operation as successful
        operation_successful = True
        # Exit the loop early since we don't need to retry anymore
        break

    # Move on to the next attempt
    attempt += 1

# After the loop, report the final outcome
if operation_successful:
    # The loop was exited early via break because it succeeded
    print("Operation completed successfully")
else:
    # The loop ran out of attempts without succeeding
    print("Operation failed after three attempts")
