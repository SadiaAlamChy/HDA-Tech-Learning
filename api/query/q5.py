from database.dbcon import PostgresConnection
import pandas as pd
class Query5:
    def __init__(self):
        self.con = PostgresConnection().getConnection()
        print("Constructor called")

    def execute(self):
        con = PostgresConnection().getConnection()
        cur = con.cursor()
        query = ''' SELECT  s.year,r.division, SUM(t.total_price) 
          FROM ecomdb_star_schema.fact_table t 
         JOIN ecomdb_star_schema.time_dim s on s.time_key = t.time_key 
		JOIN ecomdb_star_schema.store_dim r on r.store_key = t.store_key 
        GROUP BY CUBE(s.year,r.division) 
        ORDER BY s.year ASC'''
        cur.execute(query)
        result = cur.fetchall()
        pd_data = pd.DataFrame(list(result), columns=['year','division','sum'])
        #pd_data['year'] = pd_data['year'].astype('int32')
        #pd_data = pd_data.dropna()
        pd_data = pd_data[(pd_data['year'] == 2015) & (pd_data['division'] == 'BARISAL')]
        print(pd_data)
        return pd_data.to_dict(orient='records')

if __name__ == '__main__':
    q5 = Query5()
    data5 = q5.execute()
    print(data5)