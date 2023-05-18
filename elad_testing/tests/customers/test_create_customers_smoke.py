import pytest
import logging as logger
from elad_testing.src.utilities.genericUtilities import generate_random_email_and_password
from elad_testing.src.helpers.customers_helper import CustomerHelper
from elad_testing.src.dao.customers_dao import CustomersDAO


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

    # import pdb;
    # pdb.set_trace()

    # verify email and first name in the response
    assert cust_api_info['email'] == email, f"Create customer api return wrong email. Email: {email}"
    assert cust_api_info['first_name'] == '', "Create customer api returned value for first name although it needs to " \
                                              "be empty"
    cust_dao = CustomersDAO()
    cust_info = cust_dao.get_customer_by_email(email)

    id_in_api = cust_api_info['id']
    id_in_db = cust_info[0]['ID']
    assert id_in_api == id_in_db, f"Create customer response id now same as ID in db" \
                                  f"Email: {email}"

    # import pdb;
    # pdb.set_trace()

    # verify customer is created in DB
