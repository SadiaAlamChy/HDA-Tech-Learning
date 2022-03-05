from flask import jsonify,request
from flask.views import MethodView
from api.database.dbcon import PostgresConnection
import pandas as pd

class Query6(object):
    def __init__(self):
        conn = PostgresConnection()
        print("constructor")

    def execute(self):
        self.conn = PostgresConnection().getConnection()
        cur = self.conn.cursor()
        select_query = ''' select  i.supplier,i.item_name,  sum(f.quantity)  
                from ecomdb.fact_table f 
                join ecomdb.item_dim i on f.item_key=i.item_key  
                group by (i.supplier,i.item_name,f.quantity)  
                order by (i.supplier,f.quantity) desc '''
        cur.execute(select_query)
        record = cur.fetchall()
        query_6 = pd.DataFrame(list(record),columns=['supplier','item_name','quantity'])
        query_6 = query_6.set_index('item_name').groupby("supplier")['quantity'].nlargest(3).reset_index()
        # print(query_6)
        x = len(query_6)
        print(x)
        for i in range(0, x):
            if (i % 3 != 0):
                query_6.iloc[i, 0] = ''

        query_6.drop(columns=query_6.columns[-1], axis=1, inplace=True)
        return query_6.to_dict(orient='records')

if __name__ == '__main__':
    q6 = Query6()
    data = q6.execute()
    print(data)


class Query6_Api(MethodView):
    def __init__(self):
        self.q6 = Query6()

    def get(self):
        result = self.q6.execute()
        return jsonify(result)
