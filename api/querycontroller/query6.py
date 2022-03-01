from database.dbcon import PostgresConnection
import pandas as pd
class Query6:
    def __init__(self):
        self.con = PostgresConnection().getConnection()
        print("Constructor called")

    def execute(self):
        con = PostgresConnection().getConnection()
        cur = con.cursor()
        query =" SELECT s.store_key,i.item_name,SUM(f.quantity)" \
              " From ecomdb_star_schema.fact_table f " \
              " JOIN ecomdb_star_schema.store_dim s on s.store_key=f.store_key " \
              "JOIN ecomdb_star_schema.item_dim i on i.item_key=f.item_key" \
              " GROUP BY CUBE(s.store_key,i.item_name) " \
              "order by s.store_key, sum(f.quantity) DESC"
        cur.execute(query)
        result = cur.fetchall()
        pd_data = pd.DataFrame(list(result), columns=['Store_key', 'Item_name' ,'Quantity'])
        pd_data = pd_data.dropna()
        pd_data = pd_data.groupby('Store_key').head(3)
        pd_data.drop_duplicates(subset='Store_key', keep='first')
        pd_data = pd_data.head(3)
        pd_data['Quantity'] = pd_data['Quantity'].astype('int64')
        #pd_data['Item_name'] +=pd_data['Item_name']
        #pd_data['Store_key/Item_name'] = pd_data['Store_key'] + ' / ' + pd_data['Item_name']
        #print(pd_data)
        return pd_data.to_dict(orient='list')

if __name__ == '__main__':
    q6 = Query6()
    data = q6.execute()
    print(data)