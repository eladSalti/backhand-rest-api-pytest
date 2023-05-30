# We don't need to use class for the test cases but in this file I will show how to do so
import pytest
from datetime import timedelta, datetime
from elad_testing.src.helpers.products_helper import ProductsHelper
from elad_testing.src.dao.products_dao import ProductsDAO

@pytest.mark.regression
class TestListProductsWithFilter(object):
# It's very improtant to understand that we do not allow to create an constractor (init) method in this class (it will not be a test case)
    @pytest.mark.tcid51
    def test_list_product_with_filter_after(self):

        # create data - give me all the products that was created in the last 30 days
        x_days_from_today = 300
        _after_created_date = datetime.now().replace(microsecond=0) - timedelta(days=x_days_from_today)
        after_created_date = _after_created_date.isoformat()

        # make the call
        payload = dict()
        payload['after'] = after_created_date
        payload['per_page'] = 100
        rs_api = ProductsHelper().call_list_products(payload)
        assert rs_api, f"Empty response from list products with filter"
        # Get data from db
        list_of_products_from_db = ProductsDAO().get_products_after_given_date(after_created_date)
        # verify the response
        assert len(rs_api) == len(list_of_products_from_db), f"List products with filter after returned unexpected " \
                                                             f"number of products Expected: {len(list_of_products_from_db)}, Actual: {len(rs_api)}"

        ids_in_api = [i['id'] for i in rs_api]
        ids_in_db = [i['ID'] for i in list_of_products_from_db]

        ids_diff = list(set(ids_in_api) - set(ids_in_db))
        assert not ids_diff, f"List products with filter, Product ids in response mismatch in db"