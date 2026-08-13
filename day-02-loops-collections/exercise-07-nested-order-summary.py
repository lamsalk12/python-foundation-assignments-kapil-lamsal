# Define a dictionary of orders, where each order is itself a dictionary (nested)
orders = {
    "ORD-001": {
        "customer": "Anisha",
        "amount": 2500,
        "status": "Completed"
    },
    "ORD-002": {
        "customer": "Ravi",
        "amount": 1800,
        "status": "Pending"
    },
    "ORD-003": {
        "customer": "Maya",
        "amount": 3200,
        "status": "Completed"
    }
}

# 1. Print every order ID and its customer by looping over the outer dictionary
print("All orders:")
for order_id, details in orders.items():
    # Access the nested "customer" key within each order's details
    print(f"  {order_id}: {details['customer']}")

# 2. Print only completed orders by checking the nested "status" key
print("Completed orders:")
for order_id, details in orders.items():
    # Only print if the status is "Completed"
    if details["status"] == "Completed":
        print(f"  {order_id}: {details['customer']} - {details['amount']}")

# 3. Calculate the total amount of completed orders using a generator expression
total_completed_amount = sum(
    details["amount"] for details in orders.values() if details["status"] == "Completed"
)

# Print the total amount of completed orders
print(f"Total amount (completed orders): {total_completed_amount}")

# 4. Count pending orders using a generator expression with sum()
pending_count = sum(1 for details in orders.values() if details["status"] == "Pending")

# Print the count of pending orders
print(f"Pending order count: {pending_count}")

# 5. Add a new order to the dictionary
orders["ORD-004"] = {
    "customer": "Sagar",
    "amount": 4100,
    "status": "Pending"
}

# Print the updated orders dictionary to confirm the new order was added
print(f"Updated orders: {orders}")
