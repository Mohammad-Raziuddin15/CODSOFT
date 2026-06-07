contacts = {}

print("=====  CONTACT BOOK  =====")

while True:

    print("\n1. Add Contact")
    print("2. View Contact")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete contact")
    print("6. Exit")

    choice = input("\nEnter your chocie")

    #ADD CONTACT
    if choice == "1":

        name = input("Enter Name: ")
        phone =input("Enter Phone number: ")
        email = input("Enter your Email:")
        address = input("Enter Address:")
        
        contacts[name] = {
            "phone" : phone,
            "Email" : email,
            "Address" : address
        }

        print("Contact added successfully!")

    #VIEW CONTACTS
    elif choice == "2":

        if len(contacts) == 0:

            print("No contacts available.")

        else:

            print("\n===== SAVED CONTACTS  =====")

            for name, number in contacts.items():

               print(name, ":", number)


    #SEARCH CONTACT
    elif choice == "3":

        search = input("Enter Name or Phone number to search:")

        found = False

        for name, details in contacts.items():

            if search == name or search == details["phone"]:

                print("\nContact Found")
                print("Name:", name)
                print("Phone:", details["phone"])
                print("Email:", details["Email"])
                print("Address:", details["Address"])

                found = True
                break

        if not found:

            print("Contact not found.")

    # UPDATE CONTACT
    elif choice == "4":

        update_name = input("Enter contact name to update: ")

        if update_name in contacts:

            new_phone = input("Enter new phone number:")
            new_email = input("Enter new email:")
            new_address = input("Enter new address:")

            contacts[update_name] = {
                "phone" : new_phone,
                "email" : new_email,
                "address" : new_address
            }

            print("Contact not found.")

    # DELETE CONTACT
    elif choice == "5":
        delete_name = input("Enter contact name to delete:")

        if delete_name in contacts:

            del contacts[delete_name]

            print("Contact deleted successfully!")

        else:

            print("Contact not found.")

    
    # EXIT
    elif choice == "6":

        print("Contact Book Closed")

        break

    # INVALID INPUT
    else:

        print("Invalid choice. Please try again.")
