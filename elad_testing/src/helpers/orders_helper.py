import json
import os
from elad_testing.src.utilities.wooAPIUtility import WooAPIUtility

class OrdersHelper(object):

    def __init__(self):
        self.cur_file_dir = os.path.dirname(os.path.realpath(__file__))
        self.woo_helper = WooAPIUtility()

    def create_order(self, additional_args=None):

        payload_temaplte = os.path.join(self.cur_file_dir,'..','data','create_order_payload.json')

        with open(payload_temaplte) as f:
            payload = json.load(f)

        # if the user adds more info to payload, then update it
        if additional_args:
            # assert if the additional_args is a dictionary
            assert  isinstance(additional_args,dict), f"Parameter additional_args must be a dictionary but found {type(additional_args)}"
            payload.update(additional_args)


        rs_api = self.woo_helper.post('orders', params=payload, expected_status_code=201)

        return rs_api