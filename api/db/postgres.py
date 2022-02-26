import psycopg2


class PostgresConnection(object):
    def __init__(self):
        self.connection = psycopg2.connect(database="ecomdb",
                                           user="postgres",
                                           password="123456",
                                           host="127.0.0.1",
                                           port="5432")

    def get_connection(self):
        return self.connection
