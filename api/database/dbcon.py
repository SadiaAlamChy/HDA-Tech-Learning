import psycopg2


class PostgresConnection(object):
    def __init__(self):
        self.connection = psycopg2.connect(database="ecomdb",
                                           user="postgres",
                                           password="123456",
                                           host="127.0.0.1",
                                           port="5432")

    def get_connection(self):
        print("successfully connected to database")
        return self.connection

    def retrive_data_from_table(select_stmt):
        con = PostgresConnection().get_connection()
        cur = con.cursor()
        #     select_stmt = "SELECT t.payment_key , t.trans_type, t.bank_name " \
        #                   "FROM ecomdb_star_schema.trans_dim t"
        cur.execute(select_stmt)
        records = cur.fetchall()
        return records



# con = PostgresConnection().get_connection()