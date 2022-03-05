from api.database.dbcon import PostgresConnection
import pandas as pd

class Query3(object):
    def __init__(self):
        self.conn = PostgresConnection()
        print('Constructor')

    def execute(self):
        conn = PostgresConnection().getConnection()
        cur = conn.cursor()
        select_query = ''' select s.division , sum(f.total_price)
                from ecomdb.fact_table f 
                join ecomdb.store_dim s on s.store_key = f.store_key 
                where s.division = 'BARISAL' 
                group by (s.division)'''
        cur.execute(select_query)
        records = cur.fetchall()
        query_3 = pd.DataFrame(list(records), columns=['District','total_sales'])
        query_3['total_sales'] = query_3['total_sales'].astype('float')
        query_3.drop(columns=query_3.columns[0],axis = 1, inplace=True)
        # print(query_3)
        return query_3.to_dict(orient='records')

if __name__ == '__main__':
    q3 = Query3()
    data = q3.execute()
    print(data)