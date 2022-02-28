# from api.database.dbcon import PostgresConnection
# import database.dbcon
# from database import dbcon
from database.dbcon import PostgresConnection
import pandas as pd
class Query2:
    def __init__(self):
        self.con = PostgresConnection().getConnection()
        print("Constructor called")

    def execute(self):
        con = PostgresConnection().getConnection()
        cur = con.cursor()
        query = "SELECT  t.bank_name, SUM(f.total_price) as total_sale_price "\
"FROM ecomdb.fact_table as f "\
"inner JOIN ecomdb.trans_dim as t ON t.payment_key = f.payment_key "\
"GROUP BY CUBE(t.bank_name) "\
"ORDER BY total_sale_price asc"
        cur.execute(query)
        result = cur.fetchall()
        pd_data = pd.DataFrame(list(result), columns=['bank_name', 'total_sale_price'])
        pd_data['total_sale_price'] = pd_data['total_sale_price'].astype('float64')
        pd_data = pd_data.dropna()
        # print(pd_data)
        return pd_data.to_dict(orient='records')

if __name__ == '__main__':
    q2 = Query2()
    data = q2.execute()
    print(data)