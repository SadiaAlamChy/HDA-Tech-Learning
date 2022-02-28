# from api.database.dbcon import PostgresConnection
# import database.dbcon
# from database import dbcon
from database.dbcon import PostgresConnection
import pandas as pd
class Query6:
    def __init__(self):
        self.con = PostgresConnection().getConnection()
        print("Constructor called")

    def execute(self):
        con = PostgresConnection().getConnection()
        cur = con.cursor()
        query = "SELECT s.store_key as store_key, i.item_name as item_name, sum(f.quantity) as quantity_sales_for_each_item "\
"FROM ecomdb.fact_table as f "\
"JOIN ecomdb.store_dim as s on s.store_key=f.store_key "\
"JOIN ecomdb.item_dim as i on i.item_key=f.item_key "\
"GROUP BY (s.store_key, i.item_name) "\
"ORDER BY s.store_key, sum(f.quantity) desc"
        cur.execute(query)
        result = cur.fetchall()
        pd_data = pd.DataFrame(list(result), columns=['store_key', 'item_name','quantity_sales_for_each_item'])
        # pd_data['sales'] = pd_data['sales'].astype('float64')
        pd_data = pd_data.dropna()
        pd_data = pd_data.set_index('item_name').groupby("store_key")['quantity_sales_for_each_item'].nlargest(3).reset_index()
        # print(pd_data)
        return pd_data.to_dict(orient='records')

if __name__ == '__main__':
    q1 = Query1()
    data = q1.execute()
    print(data)