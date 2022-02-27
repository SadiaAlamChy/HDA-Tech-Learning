from database.dbcon import PostgresConnection
import pandas as pd
class Query1:
    def __init__(self):
        self.con = PostgresConnection().getConnection()
        print("Constructor called")

    def execute(self):
        con = PostgresConnection().getConnection()
        cur = con.cursor()
        query = '''SELECT  r.division , SUM(t.total_price)  
                         FROM ecomdb_star_schema.fact_table t  
                           JOIN ecomdb_star_schema.store_dim r ON t.store_key = r.store_key 
                           GROUP BY CUBE(r.division) 
                           ORDER BY r.division ASC;'''
        cur.execute(query)
        result = cur.fetchall()
        pd_data = pd.DataFrame(list(result), columns=['division', 'sales'])
        pd_data['sales'] = pd_data['sales'].astype('float64')
        pd_data = pd_data.dropna()
        print(pd_data)
        return pd_data.to_dict(orient='records')

if __name__ == '__main__':
    q1 = Query1()
    data = q1.execute()
    print(data)