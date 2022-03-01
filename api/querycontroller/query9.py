from database.dbcon import PostgresConnection
import pandas as pd
class Query9:
    def __init__(self):
        self.con = PostgresConnection().getConnection()
        print("Constructor called")

    def execute(self):
        con = PostgresConnection().getConnection()
        cur = con.cursor()
        query = " SELECT i.item_key,s.division,SUM(f.total_price)" \
              " From ecomdb_star_schema.fact_table f " \
              " JOIN ecomdb_star_schema.store_dim s on s.store_key=f.store_key " \
              "JOIN ecomdb_star_schema.item_dim i on i.item_key=f.item_key " \
              "Where i.item_key ='I00001' " \
              "Group by (i.item_key, s.division) " \
              "Order by (i.item_key,s.division)"
        cur.execute(query)
        result = cur.fetchall()
        pd_data = pd.DataFrame(list(result), columns=['Item_key', 'Division', 'Total_Sales'])
        pd_data['Total_Sales'] = pd_data['Total_Sales'].astype('float64')
        return pd_data.to_dict(orient='records')

if __name__ == '__main__':
    q9 = Query9()
    data = q9.execute()
    print(data)