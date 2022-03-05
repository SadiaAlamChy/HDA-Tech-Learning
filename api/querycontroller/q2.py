from api.database.dbcon import PostgresConnection
import pandas as pd

class Query2(object):
    def __init__(self):
        self.conn = PostgresConnection().getConnection()
        print('construstor called')

    def execute(self):
        conn = PostgresConnection().getConnection()
        cur = conn.cursor()
        select_query = '''select tr.trans_type , sum(f.total_price)        
                from ecomdb.fact_table f 
                join ecomdb.trans_dim tr on tr.payment_key = f.payment_key 
                group by (tr.trans_type)'''
        cur.execute(select_query)
        records = cur.fetchall()
        query_2 = pd.DataFrame(list(records), columns=['trans_type', 'total_price'])
        query_2['total_price'] = query_2['total_price'].astype('float')
        print(query_2)
        return query_2.to_dict(orient='records')

if __name__ =='__main__':
    q2 = Query2()
    data = q2.execute()
    print(data)

