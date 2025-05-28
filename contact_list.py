from contact_utils import load_contacts, save_contacts, add_contact

def main():
    contacts = load_contacts()

    while True:
        print("\nContact List Menu:")
        print("1. View Contacts")
        print("2. Add Contact")
        print("3. Save Contacts")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            if contacts:
                for idx, contact in enumerate(contacts, start=1):
                    print(f"{idx}. {contact['name']} - {contact['phone']} ({contact.get('email', 'No email for this contact')})")
            else:
                print("No contacts available.")
        
        elif choice == '2':
            name = input("Enter contact name: ").strip().title()
            phone = input("Enter contact phone: ").strip()
            email = input("Enter contact email (optional): ").strip()
            contacts = add_contact(contacts, name, phone, email)
        
        elif choice == '3':
            save_contacts(contacts)
        
        elif choice == '4':
            print("Exiting the program.")
            break
        
        else:
            print("Invalid choice. Please try again.")

main()