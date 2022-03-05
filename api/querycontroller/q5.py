from api.database.dbcon import PostgresConnection
import pandas as pd

class Query5(object):
    def __init__(self):
        conn = PostgresConnection()
        print("constructor")

    def execute(self):
        conn = PostgresConnection().getConnection()
        cur = conn.cursor()
        select_query = ''' select  s.division , t.year, sum(f.total_price) 
                from ecomdb.fact_table f 
                join ecomdb.time_dim t on f.time_key=t.time_key 
                join ecomdb.store_dim s on s.store_key = f.store_key 
                where t.year=2015  and s.division = 'BARISAL' 
                group by (t.year,s.division)'''
        cur.execute(select_query)
        records = cur.fetchall()
        query_5 = pd.DataFrame(list(records), columns=['district','Year', 'total_sales'])
        query_5['total_sales'] = query_5['total_sales'].astype('float')
        query_5.drop(columns=query_5.columns[0:2], axis=1, inplace=True)
        return query_5.to_dict(orient='records')


if __name__ == '__main__':
    q5 = Query5()
    data = q5.execute()
    print(data)