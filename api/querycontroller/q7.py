# from api.database.dbcon import PostgresConnection
# import database.dbcon
# from database import dbcon
from database.dbcon import PostgresConnection
import pandas as pd
class Query7:
    def __init__(self, days):
        self.days = days
        self.con = PostgresConnection().getConnection()
        print("Constructor called")

    def execute(self):
        con = PostgresConnection().getConnection()
        cur = con.cursor()
        query = "SELECT i.item_name, trans.trans_type "\
"FROM ecomdb.fact_table AS f "\
"JOIN ecomdb.trans_dim AS trans ON trans.payment_key=f.payment_key "\
"JOIN ecomdb.item_dim AS i ON i.item_key=f.item_key "\
"JOIN ecomdb.time_dim AS t ON t.time_key = f.time_key "\
"Where (trans.trans_type='card' or trans.trans_type='mobile') and t.datee > (CURRENT_DATE - integer '{}')".format(self.days)
        cur.execute(query)
        result = cur.fetchall()
        pd_data = pd.DataFrame(list(result), columns=['item_name', 'trans_type'])
        # pd_data['sales'] = pd_data['sales'].astype('float64')
        pd_data = pd_data.dropna()
        # print(pd_data)
        return pd_data.to_dict(orient='records')

if __name__ == '__main__':
    q7 = Query7()
    data = q7.execute()
    print(data)