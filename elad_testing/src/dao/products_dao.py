import random
from elad_testing.src.utilities.dbUtility import DBUtility


class ProductsDAO(object):

    def __init__(self):
        self.db_helper = DBUtility()

    # In this function we would like to get all users, and we pick (by default) only 1 email from there
    def get_random_product_from_db(self, qty=1):
        sql = "SELECT * FROM local.wp_posts where post_type='product';"
        rs_sql = self.db_helper.execute_select(sql)
        # return 1 email by random
        return random.sample(rs_sql, int(qty))

    def get_product_by_id(self, product_id):
        sql = f"SELECT * FROM local.wp_posts where ID = {product_id};"

        return self.db_helper.execute_select(sql)
