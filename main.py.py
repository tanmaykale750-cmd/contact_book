import json

try:
    with open("contacts.json", "r") as file:
        contacts = json.load(file)
except FileNotFoundError:
    contacts = []

while True:
    print("\nChoose one option number :-)")
    print("1 - Add contact")
    print("2 - Delete contact")
    print("3 - Update contact")
    print("4 - Search contact")
    print("5 - Show all contacts")
    print("6 - Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter name: ")
        phone = input("Enter phone: ")
        email = input("Enter email: ")
        contacts.append({"name": name, "phone": phone, "email": email})
        print(f"{name} added to contacts successfully :D")

    elif choice == "2":
        name_to_delete = input("Enter name to delete contact of: ")
        found = "no"
        for i in contacts:
            if i["name"].lower() == name_to_delete.lower():
                contacts.remove(i)
                print(f"{name_to_delete} has been successfully removed from contacts")
                found = "yes"
                break
        if found == "no":
            print("Contact not found")

    elif choice == "3":
        name_to_update = input("Enter name of contact to update: ")
        found = "no"
        for i in contacts:
            if i["name"].lower() == name_to_update.lower():
                new_name = input("Enter new name: ")
                new_phone = input("Enter new phone: ")
                new_email = input("Enter new email: ")

                i["name"] = new_name
                i["phone"] = new_phone
                i["email"] = new_email

                print(f"{name_to_update} -> {new_name} updated successfully")
                found = "yes"
                break

        if found == "no":
            print("Contact not found")

    elif choice == "4":
        search = input("Enter name to search: ")
        found = "no"
        for i in contacts:
            if i["name"][:len(search)].lower() == search.lower():
                print(i)
                found = "yes"
        if found == "no":
            print("No such contact found")

    elif choice == "5":
        if len(contacts) == 0:
            print("No contacts found.")
        else:
            print("\nAll Contacts:")
            for c in contacts:
                print(f"Name: {c['name']}, Phone: {c['phone']}, Email: {c['email']}")

    elif choice == "6":
        break

    else:
        print("No such option available")


with open("contacts.json", "w") as file:
    json.dump(contacts, file, indent=4)

print("Contacts saved. Goodbye!")
