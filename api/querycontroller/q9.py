# from api.database.dbcon import PostgresConnection
# import database.dbcon
# from database import dbcon
from database.dbcon import PostgresConnection
import pandas as pd
class Query9:
    def __init__(self):
        self.con = PostgresConnection().getConnection()
        print("Constructor called")

    def execute(self):
        con = PostgresConnection().getConnection()
        cur = con.cursor()
        query = "SELECT i.item_name, s.division, sum(f.total_price) as total_sales_price_for_each_item "\
"FROM ecomdb.fact_table as f "\
"JOIN ecomdb.store_dim as s on s.store_key=f.store_key "\
"JOIN ecomdb.item_dim as i on i.item_key=f.item_key  "\
"GROUP BY (i.item_name, s.division) "\
"ORDER BY i.item_name, total_sales_price_for_each_item desc"
        cur.execute(query)
        result = cur.fetchall()
        pd_data = pd.DataFrame(list(result), columns=['item_name', 'division','total_sales_price_for_each_item'])
        pd_data['total_sales_price_for_each_item'] = pd_data['total_sales_price_for_each_item'].astype('float64')
        pd_data = pd_data.dropna()
        # print(pd_data)
        x = (pd_data.groupby(['item_name'])
             .apply(lambda x: x[['division', 'total_sales_price_for_each_item']].to_dict('records'))
             .reset_index()
             .rename(columns={0: 'Sales'})
             .to_json(orient='records'))
        return eval(x)

        # return pd_data.to_dict(orient='records')

if __name__ == '__main__':
    q9 = Query9()
    data = q9.execute()
    print(data)