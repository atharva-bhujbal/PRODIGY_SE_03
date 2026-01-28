import json
import os

FILE_NAME = "contacts.json"

# Load contacts from file
def load_contacts():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    return {}

# Save contacts to file
def save_contacts(contacts):
    with open(FILE_NAME, "w") as file:
        json.dump(contacts, file, indent=4)

# Add contact
def add_contact(contacts):
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email address: ")

    contacts[name] = {
        "phone": phone,
        "email": email
    }
    save_contacts(contacts)
    print("Contact added successfully!\n")

# View contacts
def view_contacts(contacts):
    if not contacts:
        print("No contacts found.\n")
        return

    print("\nContact List:")
    for name, info in contacts.items():
        print(f"Name: {name}")
        print(f"Phone: {info['phone']}")
        print(f"Email: {info['email']}")
        print("-" * 20)
    print()

# Edit contact
def edit_contact(contacts):
    name = input("Enter contact name to edit: ")

    if name in contacts:
        phone = input("Enter new phone number: ")
        email = input("Enter new email address: ")

        contacts[name]["phone"] = phone
        contacts[name]["email"] = email
        save_contacts(contacts)
        print("Contact updated successfully!\n")
    else:
        print("Contact not found.\n")

# Delete contact
def delete_contact(contacts):
    name = input("Enter contact name to delete: ")

    if name in contacts:
        del contacts[name]
        save_contacts(contacts)
        print("Contact deleted successfully!\n")
    else:
        print("Contact not found.\n")

# Main menu
def main():
    contacts = load_contacts()

    while True:
        print("Contact Management System")
        print("-------------------------")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Edit Contact")
        print("4. Delete Contact")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            add_contact(contacts)
        elif choice == "2":
            view_contacts(contacts)
        elif choice == "3":
            edit_contact(contacts)
        elif choice == "4":
            delete_contact(contacts)
        elif choice == "5":
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Try again.\n")

# Run program
main()
