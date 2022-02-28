# from api.database.dbcon import PostgresConnection
# import database.dbcon
# from database import dbcon
from database.dbcon import PostgresConnection
import pandas as pd
class Query10:
    def __init__(self):
        self.con = PostgresConnection().getConnection()
        print("Constructor called")

    def execute(self):
        con = PostgresConnection().getConnection()
        cur = con.cursor()
        query = '''SELECT s.store_key, t.month, avg(f.total_price) as average_total_price
FROM ecomdb.fact_table as f
JOIN ecomdb.time_dim as t on t.time_key = f.time_key 
JOIN ecomdb.store_dim as s on s.store_key = f.store_key 
GROUP BY(s.store_key, t.month)    
ORDER BY(s.store_key)'''
        cur.execute(query)
        result = cur.fetchall()
        pd_data = pd.DataFrame(list(result), columns=['store_key', 'month', 'average_total_price'])
        # pd_data['sales'] = pd_data['sales'].astype('float64')
        pd_data = pd_data.dropna()
        # print(pd_data)
        return pd_data.to_dict(orient='records')

if __name__ == '__main__':
    q10 = Query10()
    data = q10.execute()
    print(data)