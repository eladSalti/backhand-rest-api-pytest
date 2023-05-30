from elad_testing.src.utilities.requestsUtilities import RequestsUtility


class ProductsHelper(object):

    def __init__(self):
        self.requests_utility = RequestsUtility()

    def get_product_by_id(self, product_id):
        return self.requests_utility.get(f"products/{product_id}")

    def create_product(self, payload):
        return self.requests_utility.post('products',payload=payload, expected_status_code=201)

    def call_list_products(self, payload=None):
        return self.requests_utility.get('products',payload=payload)

