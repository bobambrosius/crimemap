import pymysql
import dbconfig

class DBHelper:
    def connect(self, database="crimemap"):
            return pymysql.connect(
            host = dbconfig.db_host,
            user = dbconfig.db_user,
            passwd = dbconfig.db_password,
            db = database,
            port = 3307
            )

    def get_all_inputs(self):
        conn = self.connect()
        try:
            query = "select description from crimes;"
            with conn.cursor() as cursor:
                cursor.execute(query)
            return cursor.fetchall()
        finally:
            conn.close()
    
    def add_input(self, data):
        conn = self.connect()
        try:
            query = "INSERT INTO crimes (description) values (%s);"
            with conn.cursor() as cursor:
                cursor.execute(query, data)
                conn.commit()
        finally:
            conn.close()
             
    def clear_all(self):
        conn = self.connect()
        try:
            query = "DELETE FROM crimes;"
            with conn.cursor() as cursor:
                cursor.execute(query)
                conn.commit()
        finally:
            conn.close()
        