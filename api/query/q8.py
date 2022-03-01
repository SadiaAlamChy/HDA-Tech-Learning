from database.dbcon import PostgresConnection
import pandas as pd
class Query8:
    def __init__(self):
        self.con = PostgresConnection().getConnection()
        print("Constructor called")

    def execute(self):
        con = PostgresConnection().getConnection()
        cur = con.cursor()
        query = ''' SELECT r.item_name, p.quarter, SUM(t.total_price)
          FROM ecomdb_star_schema.fact_table t 
		  JOIN ecomdb_star_schema.item_dim r on r.item_key = t.item_key 
		  JOIN ecomdb_star_schema.time_dim p on p.time_key = t.time_key 
		  GROUP BY CUBE(r.item_name,p.quarter)
		  ORDER BY r.item_name ASC;'''
        cur.execute(query)
        result = cur.fetchall()
        pd_data = pd.DataFrame(list(result), columns=['item_name', 'quarter', 'sum'])
        print(pd_data)
        return pd_data.to_dict(orient='records')

if __name__ == '__main__':
    q8 = Query8()
    data8 = q8.execute()
    print(data8)