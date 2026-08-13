# Define the first set of dataset names
dataset_a = {
    "customer",
    "sales",
    "product",
    "employee"
}

# Define the second set of dataset names
dataset_b = {
    "sales",
    "product",
    "supplier",
    "inventory"
}

# Find all unique dataset names across both sets using union()
all_datasets = dataset_a | dataset_b

# Find datasets present in both sets using intersection()
common_datasets = dataset_a & dataset_b

# Find datasets that exist only in dataset_a using difference()
only_in_a = dataset_a - dataset_b

# Find datasets that exist only in dataset_b using difference()
only_in_b = dataset_b - dataset_a

# Print all unique dataset names (sorted for consistent, readable output)
print(f"All unique datasets: {sorted(all_datasets)}")

# Print datasets found in both groups
print(f"Datasets in both: {sorted(common_datasets)}")

# Print datasets only in dataset_a
print(f"Only in dataset_a: {sorted(only_in_a)}")

# Print datasets only in dataset_b
print(f"Only in dataset_b: {sorted(only_in_b)}")
