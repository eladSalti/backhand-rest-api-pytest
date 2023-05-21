import logging as logger
import pytest
from elad_testing.src.utilities.requestsUtilities import RequestsUtility


@pytest.mark.customers
@pytest.mark.tcid30
def test_get_all_customers():
    req_helper = RequestsUtility()
    res_api = req_helper.get('customers')

    # assert response is not empty!!
    assert res_api, f"Response of list all customers is empty"
