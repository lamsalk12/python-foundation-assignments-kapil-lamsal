user_role = "analyst"
is_active = True
requested_dataset = "sales_data"


# --- Scenario 2: Inactive user ---
# user_role = "analyst"
# is_active = False
# requested_dataset = "sales_data"

# --- Scenario 3: Role not allowed ---
# user_role = "intern"
# is_active = True
# requested_dataset = "sales_data"

# --- Scenario 4: Restricted dataset ---
# user_role = "engineer"
# is_active = True
# requested_dataset = "salary_data"

# list of allowed roles
allowed_roles = ["analyst", "data scientist", "engineer"]

# list of restricted datasets
restricted_datasets = ["salary_data", "personal_data"]

if not is_active:
    print("Access denied because the user is inactive.")
elif user_role not in allowed_roles:
    print("Access denied because the role is not allowed.")
elif requested_dataset in restricted_datasets:
    print("Access denied because the dataset is restricted.")
else:
    print("Access granted.")

