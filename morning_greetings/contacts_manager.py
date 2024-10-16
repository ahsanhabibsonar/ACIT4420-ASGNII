# contacts_manager.py
import csv
import re
class ContactsManager:
    def __init__(self,csv_file):
         self.csv_file=csv_file
         self.contacts=self._read_contacts_from_csv()

    def _read_contacts_from_csv(self):
        contacts=[]
        try:
              with open(self.csv_file,mode='r', newline='',encoding='utf-8') as file:
                   reader=csv.DictReader(file)
                   for row in reader:
                        contacts.append({
                             'name':row['name'],
                             'email':row['email'],
                             'preferred_time':row['preferred_time']
                        })
        except FileNotFoundError:
             print(f"{self.csv_file} not found. Starting with an empty contacts list")
        return contacts

    def _write_contacts_to_csv(self):
         with open(self.csv_file, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=['name', 'email', 'preferred_time'])
            writer.writeheader()
            for contact in self.contacts:
                writer.writerow(contact)

    def add_contact(self, name, email, preferred_time="08:00 AM"): # Adding basic validation for email format and time format
        """Add a new contact if it doesn't already exist."""
        # Check for duplicates
        for contact in self.contacts:
            if contact['email'] == email:
                print(f"Contact with email {email} already exists.")
                return
        if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            print("Invalid email address")
            return
        if not re.match(r"^\d{2}:\d{2} [AP]M$", preferred_time):
            print("Invalid preferred time format")
            return
        contact = {
            'name': name,
            'email': email,
            'preferred_time': preferred_time
            }
        self.contacts.append(contact)
        self._write_contacts_to_csv()
        print(f"Contact Added {name}")

    def remove_contact(self, name): # using try and except to improve efficiency
        initial_count=len(self.contacts)
        self.contacts=[c for c in self.contacts if c['name'] != name]
        if len(self.contacts)<initial_count:
             self._write_contacts_to_csv()
             print(f"contact removed{name}")
        else:
             print(f"No contact found with the name {name}")    
        
    def get_contacts(self):
            return self.contacts
        
    def list_contacts(self): # Replacing print with return
            #for contact in self.contacts:
             #   print(f"Name: {contact['name']}, Email: {contact['email']}, Preferred Time:{contact['preferred_time']}")
             return[f"Name: {contact['name']}, Email: {contact['email']}, Preferred Time:{contact['preferred_time']}" 
                    for contact in self.contacts]
    
    # Optional: Add __str__ method for representation
    def __str__(self):
        return f"ContactsManager with {len(self.contacts)} contacts."
    
