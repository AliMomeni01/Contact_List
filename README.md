Contact List Manager

This Python script allows you to manage a list of contacts, where each contact includes a name and phone number. It includes functionality to add new contacts, search for existing ones, and back up the contact list in a JSON file format. Additionally, it can load contacts from a previous backup.
Features

    Add Contact: Add new contacts with a name and phone number to the list.
    Search Contact: Search for contacts by name (case-insensitive search).
    Backup Contacts: Save your contact list as a JSON file.
    Load Previous Contacts: Load an existing contact list from a backup file.
    View Contacts: Print all the contacts currently in the list.

How It Works

    Initialization: When the program starts, it can load a list of contacts from a backup file (if provided) using the specified file path.
    Adding Contacts: The add() method allows adding new contacts with a name and phone number.
    Searching Contacts: The search() method allows searching for contacts by name, returning matching results.
    Backup Contacts: The backup() method saves the current list of contacts to a JSON file.
    View All Contacts: The print() method displays all the saved contacts.

Code Structure

    __init__(path): Initializes the contact list and optionally loads contacts from the specified path.
    add(name, number): Adds a new contact to the list.
    search(name): Searches for contacts whose names match the given input.
    backup(): Saves the current contact list to a JSON file.
    print(): Prints the list of contacts in the console.

Example Usage

python

# Create a new contact list
my_contact = Contactlist(path="D:\\Python Übung\\Folge8\\backup\\contact_list.json")

# Add contacts
my_contact.add("John Doe", "0123456789")
my_contact.add("Jane Smith", "0987654321")

# Search for a contact
my_contact.search("John")

# Backup the contact list
my_contact.backup()

# Print all contacts
my_contact.print()

File Structure

The program stores contacts in the following format in a JSON file:

json

[
  {
    "Name": "John Doe",
    "Number": "0123456789"
  },
  {
    "Name": "Jane Smith",
    "Number": "0987654321"
  }
]

Requirements

    Python 3.x#   C o n t a c t _ L i s t 
 
 
