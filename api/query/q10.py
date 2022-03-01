from database.dbcon import PostgresConnection
import pandas as pd
class Query10:
    def __init__(self):
        self.con = PostgresConnection().getConnection()
        print("Constructor called")

    def execute(self):
        con = PostgresConnection().getConnection()
        cur = con.cursor()
        query = ''' SELECT  r.item_name,p.month, SUM(t.total_price)
          FROM ecomdb_star_schema.fact_table t 
		  JOIN ecomdb_star_schema.item_dim r on r.item_key = t.item_key 
		  JOIN ecomdb_star_schema.time_dim p on p.time_key = t.time_key
		  GROUP BY CUBE(r.item_name,p.month)
		  ORDER BY r.item_name,p.month ASC;'''
        cur.execute(query)
        result = cur.fetchall()
        pd_data = pd.DataFrame(list(result), columns=['item_name', 'month', 'total_sales'])
        pd_data = pd_data[(pd_data['item_name'].isna() == False) & (pd_data['month'].isna() == False)]
        pd_data.set_index('item_name', inplace=True)
        print(pd_data)
        return pd_data.to_dict('series')

if __name__ == '__main__':
    q10 = Query10()
    data10 = q10.execute()
    print(data10)