# kivy import and runn

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

class EmergencyApp(App):
    def build(self):
        self.layout = BoxLayout(orientation='vertical')
        self.location_input = TextInput(hint_text='Enter location')
        self.contact_input = TextInput(hint_text='Enter contact number')
        save_button = Button(text='Save Contact')
        alert_button = Button(text='Send Alert')

        save_button.bind(on_press=self.save_contact)
        alert_button.bind(on_press=self.send_alert)

        self.layout.add_widget(self.location_input)
        self.layout.add_widget(self.contact_input)
        self.layout.add_widget(save_button)
        self.layout.add_widget(alert_button)

        return self.layout

    def save_contact(self, instance):
        # Logic to save contact
        pass

    def send_alert(self, instance):
        # Logic to send alert
        pass

if __name__ == '__main__':
    EmergencyApp().run()



# Sql lite code

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

if __name__ == "__main__":
    contact_manager = ContactManager()

    # Example: Adding some contacts
    contact_manager.add_contact('John Doe', '+1234567890', 'Friend')
    contact_manager.add_contact('Jane Smith', '+0987654321', 'Family')

    # Viewing and printing contacts
    contacts = contact_manager.view_contacts()
    print("Emergency Contacts:")
    for contact in contacts:
        print(f"ID: {contact[0]}, Name: {contact[1]}, Number: {contact[2]}, Relationship: {contact[3]}")

    # Close the database connection
    contact_manager.close()



# Here i imported twilio


from twilio.rest import Client

def send_alert(self, instance):
    # Assuming location and contact are set
    contact = self.contact_input.text
    location = self.location_input.text
    
    # Twilio setup
    client = Client('ACCOUNT_SID', 'AUTH_TOKEN')
    message = client.messages.create(
        body=f"Help! I'm at {location}.",
        from_='YOUR_TWILIO_NUMBER',
        to=contact
    )
    print("Alert sent!")



