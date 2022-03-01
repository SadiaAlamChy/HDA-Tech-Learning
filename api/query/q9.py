from database.dbcon import PostgresConnection
import pandas as pd
class Query8:
    def __init__(self):
        self.con = PostgresConnection().getConnection()
        print("Constructor called")

    def execute(self):
        con = PostgresConnection().getConnection()
        cur = con.cursor()
        query = ''' SELECT  r.item_name,p.division, SUM(t.total_price)
          FROM ecomdb_star_schema.fact_table t 
		  JOIN ecomdb_star_schema.item_dim r on r.item_key = t.item_key 
		  JOIN ecomdb_star_schema.store_dim p on p.store_key = t.store_key
		  GROUP BY CUBE(r.item_name,p.division)
		  ORDER BY r.item_name ASC;'''
        cur.execute(query)
        result = cur.fetchall()
        pd_data = pd.DataFrame(list(result), columns=['item_name', 'division', 'total_sales'])
        pd_data = pd_data[(pd_data['item_name'].isna() == False) & (pd_data['division'].isna() == False)]
        pd_data.set_index('item_name', inplace=True)
        print(pd_data)
        print(pd_data)
        return pd_data.to_json(orient="index")

if __name__ == '__main__':
    q8 = Query8()
    data8 = q8.execute()
    print(data8)