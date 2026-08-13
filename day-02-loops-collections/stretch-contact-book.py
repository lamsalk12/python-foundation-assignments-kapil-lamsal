# Create an empty dictionary to store contacts.
# Each key is a contact name, and each value is a nested dictionary
# containing "phone" and "email".
contacts = {}


def add_contact():
    """Prompt the user for contact details and store them."""
    # Ask for the contact's name
    name = input("Enter contact name: ").strip()

    # Ask for the contact's phone number
    phone = input("Enter phone number: ").strip()

    # Ask for the contact's email address
    email = input("Enter email address: ").strip()

    # Store the contact as a nested dictionary under their name
    contacts[name] = {"phone": phone, "email": email}

    # Confirm the contact was added
    print(f"Contact '{name}' added successfully.\n")


def search_contact():
    """Search for a contact by name and display their details if found."""
    # Ask which contact to search for
    name = input("Enter the name to search for: ").strip()

    # Use .get() so a missing contact returns None instead of raising KeyError
    contact = contacts.get(name)

    if contact:
        # Contact was found, so print their details
        print(f"Name: {name}")
        print(f"  Phone: {contact['phone']}")
        print(f"  Email: {contact['email']}\n")
    else:
        # Contact was not found, print a friendly message instead of crashing
        print(f"No contact found with the name '{name}'.\n")


def delete_contact():
    """Delete a contact by name, without crashing if it doesn't exist."""
    # Ask which contact to delete
    name = input("Enter the name to delete: ").strip()

    # Check if the contact exists before trying to delete it
    if name in contacts:
        # Remove the contact from the dictionary
        del contacts[name]
        print(f"Contact '{name}' deleted successfully.\n")
    else:
        # Avoid a KeyError by checking membership first
        print(f"No contact found with the name '{name}'.\n")


def display_contacts():
    """Display all stored contacts."""
    # Check if the contacts dictionary is empty
    if not contacts:
        print("No contacts saved yet.\n")
        return

    # Loop through every contact and print their details
    print("All contacts:")
    for name, details in contacts.items():
        print(f"  {name} - Phone: {details['phone']}, Email: {details['email']}")
    print()  # blank line for readability


# Main program loop - keeps showing the menu until the user exits
while True:
    # Display the menu options
    print("1. Add contact")
    print("2. Search contact")
    print("3. Delete contact")
    print("4. Display all contacts")
    print("5. Exit")

    # Ask the user to choose an option
    choice = input("Choose an option (1-5): ").strip()

    # Route to the correct function based on the user's choice
    if choice == "1":
        add_contact()
    elif choice == "2":
        search_contact()
    elif choice == "3":
        delete_contact()
    elif choice == "4":
        display_contacts()
    elif choice == "5":
        # Print a goodbye message and exit the loop
        print("Exiting contact book. Goodbye!")
        break
    else:
        # Handle invalid menu choices without crashing
        print("Invalid option. Please choose a number between 1 and 5.\n")
