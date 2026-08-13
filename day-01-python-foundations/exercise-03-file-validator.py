file_name = input("Enter the file name: ")

file_name = file_name.strip().lower()

valid_extensions = (".csv", ".json", ".parquet") # Acceptable file extensions

if file_name.endswith(valid_extensions):
    print(f"'{file_name}' is a valid file type.")
else:
    print(f"'{file_name}' is not a valid file type. Accepted types: .csv, .json, .parquet")
