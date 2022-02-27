from database.dbcon import PostgresConnection
import pandas as pd
class Query6:
    def __init__(self):
        self.con = PostgresConnection().getConnection()
        print("Constructor called")

    def execute(self):
        con = PostgresConnection().getConnection()
        cur = con.cursor()
        query = ''' SELECT  r.item_name, count(*) 
          FROM ecomdb_star_schema.fact_table t 
		  JOIN ecomdb_star_schema.item_dim r on r.item_key = t.item_key 
          GROUP BY CUBE(r.item_name) 
          ORDER BY r.item_name ASC
		  LIMIT 3;'''
        cur.execute(query)
        result = cur.fetchall()
        pd_data = pd.DataFrame(list(result), columns=['item_name','count'])
        print(pd_data)
        return pd_data.to_dict(orient='records')

if __name__ == '__main__':
    q6 = Query6()
    data6 = q6.execute()
    print(data6)