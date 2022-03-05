from api.database.dbcon import PostgresConnection
import pandas as pd

class Query9(object):
    def __init__(self):
        conn = PostgresConnection()

    def execute(self):
        conn = PostgresConnection().getConnection()
        cur = conn.cursor()

        select_query = ''' select   
                i.item_name,
                s.division,
                sum(f.total_price) 
                from ecomdb.fact_table f
                join ecomdb.store_dim s on s.store_key = f.store_key 
                join ecomdb.item_dim i on i.item_key = f.item_key 
                group by (i.item_name,s.division)    
                order by (i.item_name)'''
        cur.execute(select_query)
        records = cur.fetchall()
        query9 = pd.DataFrame(list(records), columns=['item_name', 'division', 'total_sales'])
        query9['total_sales'] = query9['total_sales'].astype('float')

        j = (query9.groupby(['item_name'])
             .apply(lambda x: x[['division', 'total_sales']].to_dict(orient='records'))
             .reset_index()
             .rename(columns={0: 'Sales'})
             .to_json(orient='records'))
        # print(j)
        return j

if __name__ == '__main__':
    q9 = Query9()
    q9.execute()


from flask import json
from flask.views import MethodView

class Query9_Api(MethodView):
    def __init__(self):
        self.q9 = Query9()

    def get(self):
        result = self.q9.execute()
        return (json.dumps(json.loads(result), indent=2,sort_keys=False)) #jsonify(result)