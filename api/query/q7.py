from database.dbcon import PostgresConnection
import pandas as pd
class Query7:
    def __init__(self):
        self.con = PostgresConnection().getConnection()
        print("Constructor called")

    def execute(self):
        con = PostgresConnection().getConnection()
        cur = con.cursor()
        query = ''' SELECT  r.item_name 
          FROM ecomdb_star_schema.fact_table t 
		  JOIN ecomdb_star_schema.item_dim r on r.item_key = t.item_key 
		  JOIN ecomdb_star_schema.time_dim p on p.time_key = t.time_key 
          WHERE dates > current_date - interval '90' day ORDER BY dates desc;'''
        cur.execute(query)
        result = cur.fetchall()
        pd_data = pd.DataFrame(list(result), columns=['item_name'])
        print(pd_data)
        return pd_data.to_dict(orient='records')

if __name__ == '__main__':
    q7 = Query7()
    data7 = q7.execute()
    print(data7)