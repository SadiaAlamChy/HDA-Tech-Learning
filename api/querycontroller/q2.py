#from database.dbcon import PostgresConnection
import psycopg2
import pandas as pd


class PostgresConnection(object):
    def __init__(self):
        self.connection = psycopg2.connect(database="ecomdb",
                                           user="postgres",
                                           password="afra1234",
                                           host="127.0.0.1",
                                           port="5432")

    def getConnection(self):
        print("successfully connected to database")
        return self.connection


class Query2:
    def __init__(self):
        self.con = PostgresConnection().getConnection()
        print("Constructor called")

    def execute(self):
        con = PostgresConnection().getConnection()
        cur = con.cursor()
        query = " SELECT trs.trans_type, SUM(fact.total_price) " \
            " From ecom_schema.fact_table fact " \
            " JOIN ecom_schema.trans_dim trs on trs.payment_key = fact.payment_key " \
            " GROUP BY (trs.trans_type) "
        cur.execute(query)
        result = cur.fetchall()
        pd_data = pd.DataFrame(list(result), columns=['division', 'sales'])
        pd_data['sales'] = pd_data['sales'].astype('float64')
        pd_data = pd_data.dropna()
        print(pd_data)
        # return pd_data.to_dict(orient='records')


if __name__ == '__main__':
    q2 = Query2()
    data = q2.execute()
    print(data)
