from elad_testing.src.utilities.genericUtilities import generate_random_email_and_password
from elad_testing.src.utilities.requestsUtilities import RequestsUtility


class CustomerHelper(object):
    def __init__(self):
        self.requests_utility = RequestsUtility()

    # **kwargs is if we would like to add more fields to the customer we are creating
    # we are passing an empty argument for email and password
    def create_customer(self, email=None, password=None, **kwargs):
        # This case is if we don't specify any email or password - we will just generate a random one
        if not email:
            ep = generate_random_email_and_password()
            email = ep['email']
        if not password:
            password = 'Password1'
        # create a payload as a dictionary
        payload = dict()
        payload['email'] = email
        payload['password'] = password
        # If we would like to add more fields to our customer
        payload.update(kwargs)

        create_user_json = self.requests_utility.post('customers', payload=payload, expected_status_code=201)

        return create_user_json
