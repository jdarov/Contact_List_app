import json

def load_contacts(file_path='contact_list.json'):
    """
    Load contacts from a JSON file.

    :param file_path: Path to the JSON file containing contacts.
    :return: List of contacts loaded from the file.
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            contacts = json.load(file)
        return contacts
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return []
    except json.JSONDecodeError:
        print(f"Error decoding JSON from the file: {file_path}")
        return []
    else:
        return []

def save_contacts(contacts, file_path='contact_list.json'):
    """
    Save contacts to a JSON file.

    :param contacts: List of contacts to save.
    :param file_path: Path to the JSON file where contacts will be saved.
    """
    try:
        with open(file_path, 'w') as file:
            json.dump(contacts, file, indent=4)
        print(f"Contacts saved successfully to {file_path}")
    except IOError as e:
        print(f"Error saving contacts to file: {e}")

def add_contact(contacts, name, phone, email):
    """
    Add a new contact to the list.
    If contact with the same name already exists, return the existing list without adding.

    :param contacts: List of existing contacts.
    :param name: Name of the contact.
    :param phone: Phone number of the contact.
    :param email: Email address of the contact.
    :return: Updated list of contacts with the new contact added.
    """

    for c in contacts:
        if c['name'] == name:
            print(f"Contact with name '{name}' already exists.")
            return contacts
    new_contact = {
        'name': name,
        'phone': phone,
        'email': email
    }
    contacts.append(new_contact)
    print(f"Contact '{name}' added successfully.")
    return contacts