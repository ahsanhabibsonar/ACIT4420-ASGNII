 # logger.py

import datetime
'''
def log_message(contact, message):
    with open("message_log.txt", "a") as log_file:
        log_file.write(f"{datetime.datetime.now()}- Sent to {contact['name']}: {message}\n")
'''

def log_message(contact, message, log_file_path="message_log.txt"): #log_file_path as function argument
    try:
        if 'name' not in contact:
            raise ValueError("Contact dictionary must contain a 'name' key.")

        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open(log_file_path, "a") as log_file:
            log_file.write(f"{timestamp} - Sent to {contact['name']}: {message}\n")
    except Exception as e:
        print(f"Error writing to log: {e}")
