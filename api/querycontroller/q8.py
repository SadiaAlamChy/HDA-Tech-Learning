# from api.database.dbcon import PostgresConnection
# import database.dbcon
# from database import dbcon
from sqlalchemy import column
from database.dbcon import PostgresConnection
import pandas as pd
class Query8:
    def __init__(self):
        self.con = PostgresConnection().getConnection()
        print("Constructor called")

    def execute(self):
        con = PostgresConnection().getConnection()
        cur = con.cursor()
        query = "SELECT new_table.item_name, new_table.quarter, min(total_sales_quantity_for_each_item) as minimum_sales_quantity_for_each_item "\
"FROM(SELECT i.item_name, t.quarter, sum(f.quantity) as total_sales_quantity_for_each_item "\
"FROM ecomdb.fact_table as f "\
"JOIN ecomdb.time_dim as t on t.time_key=f.time_key "\
"JOIN ecomdb.item_dim as i on i.item_key=f.item_key  "\
"GROUP BY (i.item_name, t.quarter) "\
"ORDER BY i.item_name, total_sales_quantity_for_each_item desc) as new_table "\
"GROUP BY (new_table.item_name, new_table.quarter)"
        cur.execute(query)
        result = cur.fetchall()
        pd_data = pd.DataFrame(list(result), columns=['item_name', 'quarter','minimum_sales_quantity_for_each_item'])
        # pd_data['sales'] = pd_data['sales'].astype('float64')
        pd_data = pd_data.dropna()
        pd_data = pd_data.set_index('quarter').groupby("item_name")['minimum_sales_quantity_for_each_item'].nsmallest(1).reset_index()
        # print(pd_data)
        pd_data = pd_data.drop(columns='minimum_sales_quantity_for_each_item', axis=1)
        return pd_data.to_dict(orient='records')

if __name__ == '__main__':
    q8 = Query8()
    data = q8.execute()
    print(data)