import pytest
import logging as logger
from elad_testing.src.utilities.genericUtilities import generate_random_email_and_password
from elad_testing.src.helpers.customers_helper import CustomerHelper
from elad_testing.src.dao.customers_dao import CustomersDAO
from elad_testing.src.utilities.requestsUtilities import RequestsUtility


@pytest.mark.tcid29
def test_create_costumer_only_email():
    logger.info("TEST: Create new customer with email and password")

    rand_info = generate_random_email_and_password()
    # logger.info(rand_info)
    email = rand_info['email']
    password = rand_info['password']

    # make the call
    cust_obj = CustomerHelper()
    cust_api_info = cust_obj.create_customer(email=email, password=password)

    # verify email and first name in the response
    assert cust_api_info['email'] == email, f"Create customer api return wrong email. Email: {email}"
    assert cust_api_info['first_name'] == '', "Create customer api returned value for first name although it needs to " \
                                              "be empty"

    # verify customer is created in DB
    cust_dao = CustomersDAO()
    cust_info = cust_dao.get_customer_by_email(email)

    id_in_api = cust_api_info['id']
    id_in_db = cust_info[0]['ID']
    assert id_in_api == id_in_db, f"Create customer response id now same as ID in db" \
                                  f"Email: {email}"

@pytest.mark.tcid47
def test_create_customer_fail_for_existing_email():
    # get existing email from db
    cust_dao = CustomersDAO()
    existing_cust = cust_dao.get_random_customer_from_db()
    existing_email = existing_cust[0]['user_email']

    # call the API
    # cust_obj = CustomerHelper()
    # cust_api_info = cust_obj.create_customer(email=existing_email, password="Password1")

    req_helper = RequestsUtility()

    payload = {"email": existing_email, "password": "Password1"}
    cust_api_info = req_helper.post(endpoint='customers', payload=payload, expected_status_code=400)

    assert cust_api_info['code'] == 'registration-error-email-exists', f"Create customer with existing user error " \
                                                                       f"code is not correct. Expected " \
                                                                       f"registration-error-email-exists, " \
                                                                       f"Actual {cust_api_info['code']}"
    #
    # assert cust_api_info['message'] == 'An account is already registered with your email address', f"Create customer with existing user error " \
    #                                                                    f"code is not correct. Expected " \
    #                                                                    f"registration-error-email-exists, " \
    #                                                                    f"Actual {cust_api_info['message']}"




