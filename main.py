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
