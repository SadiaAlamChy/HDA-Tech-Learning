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
        # replace the month number into Name
        pd_data['month'] = pd_data['month'].replace(1, 'January')
        pd_data['month'] = pd_data['month'].replace(2, 'February')
        pd_data['month'] = pd_data['month'].replace(3, 'March')
        pd_data['month'] = pd_data['month'].replace(4, 'April')
        pd_data['month'] = pd_data['month'].replace(5, 'May')
        pd_data['month'] = pd_data['month'].replace(6, 'June')
        pd_data['month'] = pd_data['month'].replace(7, 'July')
        pd_data['month'] = pd_data['month'].replace(8, 'August')
        pd_data['month'] = pd_data['month'].replace(9, 'September')
        pd_data['month'] = pd_data['month'].replace(10, 'October')
        pd_data['month'] = pd_data['month'].replace(11, 'November')
        pd_data['month'] = pd_data['month'].replace(12, 'December')
        x = (pd_data.groupby(['store_key'])
             .apply(lambda x: x[['month', 'average_total_price']].to_dict('records'))
             .reset_index()
             .rename(columns={0: 'Sales'})
             .to_json(orient='records'))
        return eval(x)
        # return pd_data.to_dict(orient='records')

if __name__ == '__main__':
    q10 = Query10()
    data = q10.execute()
    print(data)