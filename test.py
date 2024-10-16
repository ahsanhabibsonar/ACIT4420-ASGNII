from morning_greetings.contacts_manager import ContactsManager
from morning_greetings.message_sender import send_message
from morning_greetings.logger import log_message
from morning_greetings.message_generator import generate_message 

def test_contacts_manager():
    # Initialize the ContactsManager with the sample CSV file
    manager = ContactsManager('csv_file/contacts.csv')
    
    # Test list_contacts method (Initial state)
    print("\nInitial contacts list:")
    contacts = manager.list_contacts()
    for contact in contacts:
        print(contact)

    # Add new contact and test add_contact
    print("\nAdding a new contact (Ashirah)...")
    manager.add_contact('Ashirah', 'ashirah@example.com', '07:00 AM')
    
    # List contacts after adding
    print("\nContacts list after adding Ashirah:")
    contacts = manager.list_contacts()
    for contact in contacts:
        print(contact)

    # Remove a contact and test remove_contact
    print("\nRemoving a contact (Alice)...")
    manager.remove_contact('Alice')
    
    # List contacts after removing
    print("\nUpdated contacts list: ")
    contacts = manager.list_contacts()
    for contact in contacts:
        print(contact)

def test_generate_message():
    name= 'Leila'
    preferred_time= '07:00 AM'
    message = generate_message(name,preferred_time)
    print(message)

def test_send_message():
    # Test sending a message
    try:
        email = 'test@example.com'
        message = 'Hello, this is a test message!'
        result = send_message(email, message)
        #print(f"Result of send message:{result}")
        if result:
            print(f"Message sending OK.")
        else:
            print(f"Failed to send message to {email}.")
    except ValueError as e:
        print(f"Error: {e}")
def test_logger():
    # timestap of sent message
    try:
        contact= {'name':'Ahsan'}
        message ='Good Morning'
        log = log_message(contact,message)

        if log is None: #Log message does not a value, so check if None
            print(f"Message log has been recorded")
        else:
            print("Failed to send message to {contact}")
    except ValueError as e:
        print(f"Error:{e}")




# Run the test function
if __name__ == "__main__":
    test_contacts_manager()
    test_generate_message()
    test_send_message()
    test_logger()
    
    
