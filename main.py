# main.py

from morning_greetings.contacts_manager import ContactsManager
from morning_greetings.message_generator import generate_message
from morning_greetings.message_sender import send_message
from morning_greetings.logger import log_message

# Set up logging at the start of your main.py
#logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def main():
    # Initialize the contacts manager
    contact_manager = ContactsManager('csv_file/contacts.csv')
    
    # Load contacts from the CSV file or start with an empty list
    contacts = contact_manager.get_contacts()
    
    if not contacts:
        print("csv_file not found. Starting with an empty contacts list")
        # Add some contacts
        contact_manager.add_contact("Alice", "alice@example.com")
        contact_manager.add_contact("Bob", "bob@example.com")
        contact_manager.add_contact("Charlie", "charlie@example.com")

        # Get updated contacts list
        contacts = contact_manager.get_contacts()

    # Send a message to each contact
    for contact in contacts:
        message = generate_message(contact['name'],contact['preferred_time'])
        email = contact['email'] # Extract  the email
        send_message(email, message) # Send message using the email
        log_message(contact, message) # log the message

if __name__ == "__main__":
    main()
