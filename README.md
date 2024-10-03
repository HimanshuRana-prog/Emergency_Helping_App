# Emergency_Helping_App
EmergencyApp is a user-friendly mobile application built with Kivy that enables users to manage emergency contacts and send alerts quickly in critical situations. The app features a simple interface with a vertical layout, allowing for easy navigation and interaction.

Key Features:
Location Input: Users can manually enter their current location, which is crucial when requesting help or notifying emergency contacts.

Emergency Contact Management: Users can input and save emergency contact numbers. The app securely stores these contacts in a SQLite database for quick access.

Alert System: The app includes a functionality to send help alerts. When the user presses the "Send Help Alert" button, the app checks for network connectivity. If a connection is available, it simulates sending an alert with the provided location. If not, the app stores the alert for later transmission.

Simple Interface: Designed with a clean and intuitive interface, the app uses Kivy’s BoxLayout for organized arrangement of input fields and buttons.

Technical Overview:
Kivy Framework: The app leverages the Kivy framework to create a responsive and interactive user interface.

SQLite Database: Emergency contacts are stored in an SQLite database, ensuring data persistence even after the app is closed.

Network Requests: Utilizes the requests library to check for internet connectivity, enhancing reliability during emergencies.

Usage:
Input Location: Enter your current location in the provided text input.
Save Contact: Enter an emergency contact number and click "Save Contact" to store it.
Send Alert: Click "Send Help Alert" to attempt to send an alert from your location. The app will handle connectivity issues and store the alert if no network is available.