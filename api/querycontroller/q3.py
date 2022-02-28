# from api.database.dbcon import PostgresConnection
# import database.dbcon
# from database import dbcon
from database.dbcon import PostgresConnection
import pandas as pd
class Query3:
    def __init__(self):
        self.con = PostgresConnection().getConnection()
        print("Constructor called")

    def execute(self):
        con = PostgresConnection().getConnection()
        cur = con.cursor()
        query = "SELECT  s.division, SUM(f.total_price) as total_sale_price "\
"FROM ecomdb.fact_table as f "\
"inner JOIN ecomdb.store_dim as s ON s.store_key = f.store_key "\
"WHERE s.division ='BARISAL' "\
"GROUP BY CUBE(s.division)"
        cur.execute(query)
        result = cur.fetchall()
        pd_data = pd.DataFrame(list(result), columns=['division', 'total_sale_price'])
        pd_data['total_sale_price'] = pd_data['total_sale_price'].astype('float64')
        pd_data = pd_data.dropna()
        # print(pd_data)
        return pd_data.to_dict(orient='records')

if __name__ == '__main__':
    q3 = Query3()
    data = q3.execute()
    print(data)