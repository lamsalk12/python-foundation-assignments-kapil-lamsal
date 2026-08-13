# Define the list of monthly sales figures
monthly_sales = [85000, 120000, 95000, 140000, 75000, 160000]

# 1. Create a sorted list from highest to lowest using sorted() with reverse=True
sales_sorted_desc = sorted(monthly_sales, reverse=True)

# 2. Create a list containing only values above 100000 using a list comprehension
high_sales = [amount for amount in monthly_sales if amount > 100000]

# 3. Create a list where each amount has 13% tax added, using a list comprehension
sales_with_tax = [amount * 1.13 for amount in monthly_sales]

# 4. Calculate the total sales amount using sum()
total_sales = sum(monthly_sales)

# 5. Calculate the average sales amount (total divided by count)
average_sales = total_sales / len(monthly_sales)

# Print the sorted (highest to lowest) list
print(f"Sorted (highest to lowest): {sales_sorted_desc}")

# Print the list of sales above 100000
print(f"Sales above 100000: {high_sales}")

# Print the list of sales with 13% tax added, rounded to 2 decimals for readability
print(f"Sales with 13% tax: {[round(amount, 2) for amount in sales_with_tax]}")

# Print the total sales amount
print(f"Total sales: {total_sales}")

# Print the average sales amount formatted to 2 decimal places
print(f"Average sales: {average_sales:.2f}")
