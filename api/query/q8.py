from api.database.dbcon import PostgresConnection
import pandas as pd
class Query8:
    def __init__(self):
        self.con = PostgresConnection().getConnection()
        print("Constructor called")

    def execute(self):
        con = PostgresConnection().getConnection()
        cur = con.cursor()
        s_quarter = "SELECT i.item_name, tim.quarter, SUM(ft.total_price) " \
                    "FROM ecomdb_star_schema.fact_table ft " \
                    "JOIN ecomdb_star_schema.item_dim i on i.item_key=ft.item_key " \
                    "JOIN ecomdb_star_schema.time_dim tim on tim.time_key = ft.time_key " \
                    "GROUP BY i.item_name, tim.quarter " \
                    "ORDER BY i.item_name, sum(ft.total_price)"
        cur.execute(s_quarter)
        sq = cur.fetchall()
        quarter_info = pd.DataFrame(list(sq), columns=['item', 'quarter', 'sales'])
        quarter_info = quarter_info.dropna()
        quarter_info = quarter_info.groupby('item').head(1)
        quarter_info.pop('sales')
        # print(pd_data)
        return quarter_info.to_dict(orient='records')

if __name__ == '__main__':
    q8 = Query8()
    data = q8.execute()
    print(data)