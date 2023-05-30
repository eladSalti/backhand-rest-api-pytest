import logging as logger
import pytest
from elad_testing.src.dao.products_dao import ProductsDAO
from elad_testing.src.helpers.products_helper import ProductsHelper
from elad_testing.src.utilities.requestsUtilities import RequestsUtility

pytestmark = [pytest.mark.products, pytest.mark.smoke]

@pytest.mark.tcid24
def test_get_all_products():
    req_helper = RequestsUtility()
    res_api = req_helper.get('products')

    # assert response is not empty!!
    assert res_api, f"Response of list all products is empty"


@pytest.mark.tcid25
def test_get_product_by_id():
    # Get a random product from DB
    product_dao = ProductsDAO()
    existing_random_prod = product_dao.get_random_product_from_db()
    existing_product_id = existing_random_prod[0]['ID']

    # Make the api call
    product_helper = ProductsHelper()
    product_response = product_helper.get_product_by_id(existing_product_id)

    # verify the response
    assert product_response['name'] == existing_random_prod[0]['post_title'], f"Get product by id returned wrong product. Id:{existing_product_id} " \
                                                                              f"Db name {existing_random_prod[0]['post_title']}," \
                                                                              f" API name: {product_response['name']}"
