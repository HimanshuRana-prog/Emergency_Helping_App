import sqlite3

class ContactManager:
    def __init__(self):
        # Setup SQLite database
        self.conn = sqlite3.connect('contacts.db')
        self.cursor = self.conn.cursor()
        self.cursor.execute('CREATE TABLE IF NOT EXISTS contacts (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, number TEXT, relationship TEXT)')
        self.conn.commit()

    def add_contact(self, name, number, relationship):
        self.cursor.execute('INSERT INTO contacts (name, number, relationship) VALUES (?, ?, ?)', (name, number, relationship))
        self.conn.commit()

    def view_contacts(self):
        self.cursor.execute('SELECT * FROM contacts')
        return self.cursor.fetchall()

    def close(self):
        self.conn.close()

def main():
    contact_manager = ContactManager()

    while True:
        # Prompt user for contact details
        name = input("Enter contact name (or type 'exit' to quit): ")
        if name.lower() == 'exit':
            break
        number = input("Enter contact number: ")
        relationship = input("Enter relationship: ")

        # Add the contact
        contact_manager.add_contact(name, number, relationship)

        # Display current contacts
        print("\nEmergency Contacts:")
        contacts = contact_manager.view_contacts()
        for contact in contacts:
            print(f"ID: {contact[0]}, Name: {contact[1]}, Number: {contact[2]}, Relationship: {contact[3]}")

    # Close the database connection
    contact_manager.close()

if __name__ == "__main__":
    main()
