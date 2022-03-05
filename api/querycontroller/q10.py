import json

from api.database.dbcon import PostgresConnection
import pandas as pd
from flask import jsonify
from flask.views import MethodView

class Query10(object):
    def __init__(self):
        conn = PostgresConnection()

    def execute(self):
        conn = PostgresConnection().getConnection()
        cur = conn.cursor()

        select_query = ''' select   
                s.store_key,
                t.month,
                avg(f.total_price) 
                from ecomdb.fact_table f
                join ecomdb.time_dim t on t.time_key = f.time_key 
                join ecomdb.store_dim s on s.store_key = f.store_key 
                group by (s.store_key,t.month)    
                order by (s.store_key)'''
        cur.execute(select_query)
        records = cur.fetchall()
        query10 = pd.DataFrame(list(records),columns=['store_key','month','avg sales'])
        # print(query10)
        j = (query10.groupby(['store_key'])
             .apply(lambda x: x[['month', 'avg sales']].to_dict(orient='records'))
             .reset_index()
             .rename(columns={0: 'Sales'})
             .to_json(orient='records'))
        # print (json.dumps(json.loads(j),indent=2))
        return j  #query10.to_dict(orient='records')

if __name__ == '__main__':
    q10 = Query10()
    q10.execute()


class Query10_Api(MethodView):
    def __init__(self):
        self.q10=Query10()

    def get(self):
        result = self.q10.execute()
        return (json.dumps(json.loads(result),indent=2)) #jsonify(result)
