from api.database.dbcon import PostgresConnection
import pandas as pd

class Query4(object):
    def __init__(self):
        self.conn = PostgresConnection()
        print("constructor")

    def execute(self):
        conn = PostgresConnection().getConnection()
        cur = conn.cursor()
        select_query  = ''' select  t.year, sum(f.total_price) 
                from ecomdb.fact_table f 
                join ecomdb.time_dim t on f.time_key=t.time_key 
                where t.year=2015 
                group by t.year '''
        cur.execute(select_query)
        records = cur.fetchall()
        query_4 = pd.DataFrame(list(records), columns=['Year', 'total_sales'])
        query_4['total_sales'] = query_4['total_sales'].astype('float')
        query_4.drop(columns=query_4.columns[0], axis=1, inplace=True)
        # print(query_3)
        return query_4.to_dict(orient='records')

if __name__ == '__main__':
    q4 = Query4()
    data = q4.execute()
    print(data)

