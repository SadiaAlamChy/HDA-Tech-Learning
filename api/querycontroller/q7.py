from api.database.dbcon import PostgresConnection
import pandas as pd

class Query7(object):
    def __init__(self, days):
        self.days = days
        self.conn = PostgresConnection()
        print("constructor")

    def execute(self):
        conn = PostgresConnection().getConnection()
        cur = conn.cursor()
        select_query = ''' select i.item_name 
                from ecomdb.fact_table f 
                join ecomdb.trans_dim t on t.payment_key=f.payment_key 
                join ecomdb.item_dim i on i.item_key=f.item_key 
                join ecomdb.time_dim td on td.time_key = f.time_key 
                where (t.trans_type='card')
                and td.date > (CURRENT_DATE - integer '{}')'''.format(self.days)
        cur.execute(select_query)
        records = cur.fetchall()
        print(records)
        # query_7 = pd.DataFrame(list(records), columns=['district','Year', 'total_sales'])
        # query_7['total_sales'] = query_7['total_sales'].astype('float')
        # query_7.drop(columns=query_7.columns[0:2], axis=1, inplace=True)
        # return query_7.to_dict(orient='records')
        pd_data = pd.DataFrame(list(records), columns=['Items'])
        print(pd_data)
        return {"item names": pd_data['Items'].tolist()}

# if __name__ == '__main__':
#     q5 = Query7(days=0)
#     data = q5.execute()
#     print(data)
