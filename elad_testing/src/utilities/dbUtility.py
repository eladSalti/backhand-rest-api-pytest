import pymysql
import logging as logger
from elad_testing.src.configs.passwords import DB_AUTH


class DBUtility(object):

    def __init__(self):
        self.host = 'localhost'

    def create_connection(self):
        connection = pymysql.connect(host=self.host, user=DB_AUTH["Username"], password=DB_AUTH["Password"], port=10006)
        return connection


    # def execute_select(self, sql):
    #     conn = self.create_connection()
    #     try:
    #         cur = conn.cursor(pymysql.cursers.DictCursor)
    #         cur.execute(sql)
    #         rs_dict = cur.fetchall()
    #         cur.close()
    #     except Exception as e:
    #         raise Exception(f"Failed Running sql: {sql} \n Error: {str(e)}")
    #     finally:
    #         conn.close()
    #     return rs_dict

    def execute_select(self, sql):
        try:
            logger.debug(f"Executing: {sql}")
            conn = self.create_connection()
            cur = conn.cursor(pymysql.cursors.DictCursor)
            cur.execute(sql)
            rs_dict = cur.fetchall()
        except pymysql.Error as e:
            raise Exception(f"Failed running SQL: {sql}\nError: {str(e)}")
        finally:
            cur.close()
            conn.close()
        return rs_dict

    def execute_sql(self, sql):
        pass
