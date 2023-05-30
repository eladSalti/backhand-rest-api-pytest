import logging as logger
import random
import string


def generate_random_email_and_password(domain=None, email_prefix=None):
    logger.debug("Generating random email and password")

    if not domain:
        domain = 'eladistheking.com'
    if not email_prefix:
        email_prefix = 'testuser'

    random_email_string_length = 10
    random_strings = ''.join(random.choices(string.ascii_lowercase, k=random_email_string_length))

    email = email_prefix + '_' + random_strings + '@' + domain

    password_length = 20
    password_string = ''.join(random.choices(string.ascii_letters, k=password_length))

    random_info = {'email': email, 'password': password_string}
    logger.debug(f"Randomly generated email and password: {random_info}")

    return random_info

def generate_random_string(length=10, prefix = None, suffix = None):

    random_strings = ''.join(random.choices(string.ascii_lowercase, k=length))

    if prefix:
        random_strings = prefix + random_strings
    if suffix:
        random_strings = random_strings + suffix

    return random_strings