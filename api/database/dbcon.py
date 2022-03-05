import psycopg2

class PostgresConnection(object):
    def __init__(self):
        self.connection = psycopg2.connect(database="ecomdb",
                                           user="postgres",
                                           password="123456",
                                           host="127.0.0.1",
                                           port="5433")

    def getConnection(self):
        print("successfully connected to database ")
        return self.connection
conn = PostgresConnection().getConnection()