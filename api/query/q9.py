from api.database.dbcon import PostgresConnection
import pandas as pd
class Query9:
    def __init__(self):
        self.con = PostgresConnection().getConnection()
        print("Constructor called")

    def execute(self):
        con = PostgresConnection().getConnection()
        cur = con.cursor()
        select_items = "SELECT i.item_name, s.division, sum(ft.total_price) " \
                       "FROM ecomdb_star_schema.fact_table ft " \
                       "JOIN ecomdb_star_schema.item_dim i on i.item_key=ft.item_key " \
                       "JOIN ecomdb_star_schema.store_dim s on s.store_key = ft.store_key " \
                       "GROUP BY CUBE(i.item_name, s.division) " \
                       "ORDER BY i.item_name,s.division "
        cur.execute(select_items)
        itemsdiv = cur.fetchall()
        idiv = pd.DataFrame(list(itemsdiv), columns=['Item', 'Division', 'Sales'])
        idiv = idiv.dropna()
        idiv.set_index('Item', inplace=True)
        # print(pd_data)
        return {"sales":idiv.to_dict(orient='records')}
        #return idiv.to_dict(orient='records')

if __name__ == '__main__':
    q9 = Query9()
    data = q9.execute()
    print(data)