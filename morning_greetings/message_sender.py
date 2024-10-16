# message_sender.py

import logging
import re

# Set up logger
logger = logging.getLogger(__name__)

def is_valid_email(email):
    email_regex = r'^[\w\.-]+@[\w\.-]+\.\w+$'  # A simple regex for email validation
    return re.match(email_regex, email) is not None

def send_message(email, message):
    if not is_valid_email(email):
        logger.error(f"Invalid email address: {email}")
        return False
    logger.info(f"Sending message to {email}: {message}")
    # Simulate sending the message
    print(f"Message sent to {email}: {message}")
    return True

