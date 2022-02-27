from database.dbcon import PostgresConnection
import pandas as pd
class Query3:
    def __init__(self):
        self.con = PostgresConnection().getConnection()
        print("Constructor called")

    def execute(self):
        con = PostgresConnection().getConnection()
        cur = con.cursor()
        query = '''SELECT    s.division, SUM(t.total_price) 
          FROM ecomdb_star_schema.fact_table t
         JOIN ecomdb_star_schema.store_dim s on s.store_key = t.store_key
		 JOIN ecomdb_star_schema.item_dim r on r.item_key = t.item_key 
		 GROUP BY CUBE( s.division) 
		 ORDER BY SUM(t.total_price) DESC;'''
        cur.execute(query)
        result = cur.fetchall()
        pd_data = pd.DataFrame(list(result), columns=['division', 'sum'])
        pd_data['sum'] = pd_data['sum'].astype('float64')
        pd_data = pd_data.dropna()
        pd_data = pd_data[(pd_data['division'] == 'BARISAL')]
        print(pd_data)
        return pd_data.to_dict(orient='records')

if __name__ == '__main__':
    q3 = Query3()
    data3 = q3.execute()
    print(data3)