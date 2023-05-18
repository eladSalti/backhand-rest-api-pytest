import random
from elad_testing.src.utilities.dbUtility import DBUtility


class CustomersDAO(object):

    def __init__(self):
        self.db_helper = DBUtility()

    # In this function we would like to get customer details by email
    def get_customer_by_email(self, email):
        """

        :param email:
        :return:
        """
        sql = f"SELECT * FROM local.wp_users WHERE user_email = '{email}';"
        rs_sql = self.db_helper.execute_select(sql)

        return rs_sql

    # In this function we would like to get all users, and we pick (by default) only 1 email from there
    def get_random_customer_from_db(self, qty=1):
        sql = "SELECT * FROM local.wp_users ORDER BY id DESC LIMIT 5000;"
        rs_sql = self.db_helper.execute_select(sql)
        # return 1 email by random
        return random.sample(rs_sql, int(qty))
