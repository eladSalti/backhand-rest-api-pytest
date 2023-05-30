import os
from woocommerce import API
from elad_testing.src.configs.passwords import API_AUTH
from elad_testing.src.configs.hosts_config import WOO_API_HOSTS
import logging as logger

class WooAPIUtility(object):

    def __init__(self):
        # We would like to set the test env as the default env unless we will override with another env
        self.env = os.environ.get('ENV', 'test')
        self.base_url = WOO_API_HOSTS[self.env]
        # As we already did in Postman we need to add OAuth 1.0 in order to make a post API call Please note that in
        # this case I decided to create a password file with all of my keys but this file is actually in the
        # .gitignore file in that case you will need to create it by yourself
        #self.auth = OAuth1(API_AUTH["Consumer Key"], API_AUTH["Consumer Secret"])

        self.wcapi = API(
            url=self.base_url,
            consumer_key=API_AUTH["Consumer Key"],
            consumer_secret=API_AUTH["Consumer Secret"],
            version="wc/v3"
        )

    def assert_status_code(self):
        assert self.status_code == self.expected_status_code, f"Bad status code. " \
                                                              f"Expected {self.expected_status_code}, Actual status code: {self.status_code}," \
                                                              f"URL: {self.url}, Response Json: {self.rs_json}"

    def get(self, wc_endpoint, params = None, expected_status_code = 200):

        rs_api = self.wcapi.get(wc_endpoint, params=params)

        self.status_code = rs_api.status_code
        self.expected_status_code = expected_status_code
        self.rs_json = rs_api.json()
        self.assert_status_code()

        logger.debug(f"API POST response: {self.rs_json}")

        return self.rs_json


# In this case if we would like to run the
if __name__ == '__main__':
    obj = WooAPIUtility()
    rs_api = obj.get('products')
    print(rs_api)
    import pdb; pdb.set_trace()