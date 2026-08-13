rows_loaded = 9800

rows_failed = 200

runtime_minutes = 18


# Test Case 2
# rows_loaded = 9500
# rows_failed = 500
# runtime_minutes = 15

# Test Case 3
# rows_loaded = 9900
# rows_failed = 100
# runtime_minutes = 30

total_rows = rows_loaded + rows_failed

failure_rate = (rows_failed / total_rows) * 100

if failure_rate <= 2 and runtime_minutes <= 20:
    status = "Healthy"
elif failure_rate <= 5:
    status = "Warning"
else:
    status = "Critical"

print(f"Failure rate: {failure_rate:.2f}%")

print(f"Pipeline status: {status}")

