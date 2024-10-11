# kivy import and runn

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from twilio.rest import Client
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.webview import WebView
import sqlite3


class ContactManager:
    def __init__(self):
        self.conn = sqlite3.connect('contacts.db')
        self.cursor = self.conn.cursor()
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS contacts (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                number TEXT,
                relationship TEXT
            )
        ''')
        self.conn.commit()

    def add_contact(self, name, number, relationship):
        self.cursor.execute('INSERT INTO contacts (name, number, relationship) VALUES (?, ?, ?)',
                            (name, number, relationship))
        self.conn.commit()

    def get_contact(self, name):
        self.cursor.execute('SELECT number FROM contacts WHERE name = ?', (name,))
        return self.cursor.fetchone()

    def close(self):
        self.conn.close()

class EmergencyApp(App):
    def build(self):
        self.contact_manager = ContactManager()
        self.layout = BoxLayout(orientation='vertical')
        self.location_input = TextInput(hint_text='Enter location')
        self.contact_input = TextInput(hint_text='Enter contact number')
        save_button = Button(text='Save Contact')
        alert_button = Button(text='Send Alert')
        self.status_label = Label(text='')

        save_button.bind(on_press=self.save_contact)
        alert_button.bind(on_press=self.send_alert)

        self.layout.add_widget(self.location_input)
        self.layout.add_widget(self.contact_input)
        self.layout.add_widget(save_button)
        self.layout.add_widget(alert_button)
        self.layout.add_widget(self.status_label)

        return self.layout

    def save_contact(self, instance):
        # Dummy example for saving a contact
        name = self.contact_input.text
        number = input("Enter the contact number: ")  # Get number from the console for simplicity
        relationship = input("Enter the relationship: ")  # Get relationship from the console
        self.contact_manager.add_contact(name, number, relationship)
        self.status_label.text = f"Saved contact: {name}"

    def send_alert(self, instance):
        contact_name = self.contact_input.text
        location = self.location_input.text
        contact = self.contact_manager.get_contact(contact_name)

        if contact:
            self.send_twilio_alert(contact[0], location)
            self.status_label.text = "Alert sent!"
        else:
            self.status_label.text = "Contact not found."

    def send_twilio_alert(self, to_number, location):
        client = Client('ACCOUNT_SID', 'AUTH_TOKEN')
        message = client.messages.create(
            body=f"Help! I'm at {location}.",
            from_='YOUR_TWILIO_NUMBER',
            to=to_number
        )


if __name__ == '__main__':
    EmergencyApp().run()






