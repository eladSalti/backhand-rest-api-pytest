import requests
import os
import json
import logging as logger
from elad_testing.src.configs.hosts_config import API_HOSTS
from elad_testing.src.configs.passwords import API_AUTH
from requests_oauthlib import OAuth1


class RequestsUtility(object):

    def __init__(self):
        # We would like to set the test env as the default env unless we will override with another env
        self.env = os.environ.get('ENV', 'test')
        self.base_url = API_HOSTS[self.env]
        # As we already did in Postman we need to add OAuth 1.0 in order to make a post API call Please note that in
        # this case I decided to create a password file with all of my keys but this file is actually in the
        # .gitignore file in that case you will need to create it by yourself
        self.auth = OAuth1(API_AUTH["Consumer Key"], API_AUTH["Consumer Secret"])

    def assert_status_code(self):
        assert self.status_code == self.expected_status_code, f"Bad status code. " \
                                                              f"Expected {self.expected_status_code}, Actual status code: {self.status_code}," \
                                                              f"URL: {self.url}, Response Json: {self.rs_json}"

    def post(self, endpoint, payload=None, headers=None, expected_status_code=200):
        if not headers:
            headers = {"Content-Type": "application/json"}

        self.url = self.base_url + endpoint

        rs_api = requests.post(self.url, data=json.dumps(payload), headers=headers, auth=self.auth)

        self.status_code = rs_api.status_code
        self.expected_status_code = expected_status_code
        self.rs_json = rs_api.json()
        self.assert_status_code()

        logger.debug(f"API POST response: {self.rs_json}")

        return self.rs_json

    def get(self, endpoint, payload=None, headers=None, expected_status_code=200):
        if not headers:
            headers = {"Content-Type": "application/json"}

        self.url = self.base_url + endpoint
        rs_api = requests.get(self.url, data=json.dumps(payload), headers=headers, auth=self.auth)

        self.status_code = rs_api.status_code
        self.expected_status_code = expected_status_code
        self.rs_json = rs_api.json()
        self.assert_status_code()

        logger.debug(f"API GET response: {self.rs_json}")

        return self.rs_json