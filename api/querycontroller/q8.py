from api.database.dbcon import PostgresConnection
import pandas as pd
from flask import jsonify
from flask.views import MethodView

class Query8(object):
    def __init__(self):
        # conn = PostgresConnection().getConnection()
        # cur = conn.cursor()
        print("constructor")

    def execute(self):
        conn = PostgresConnection().getConnection()
        cur = conn.cursor()
        select_query = ''' select i.item_name, 
                t.quarter,  
                sum(f.quantity) 
                from ecomdb.fact_table f 
                join ecomdb.item_dim i on i.item_key = f.item_key 
                join ecomdb.time_dim t on t.time_key = f.time_key 
                group by (i.item_name , t.quarter ) 
                order by (i.item_name)'''

        cur.execute(select_query)
        records = cur.fetchall()
        # print(records)
        query8 = pd.DataFrame(list(records),columns=['item_name','quarter','quantity'])
        query8 = query8.set_index('quarter').groupby("item_name")['quantity'].nsmallest(1).reset_index()
        query8.drop(columns=query8.columns[-1], axis=1, inplace=True)
        return query8.to_dict(orient='records')


if __name__ == '__main__':
    q8 = Query8()
    data = q8.execute()
    print(data)


class Query8_Api(MethodView):
    def __init__(self):
        self.q8= Query8()

    def get(self):
        result = self.q8.execute()
        return jsonify(result)