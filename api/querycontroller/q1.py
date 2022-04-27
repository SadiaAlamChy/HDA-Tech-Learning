from database.dbcon import PostgresConnection
import pandas as pd
class Query1:
    def __init__(self):
        self.con = PostgresConnection().getConnection()
        print("Constructor called")

    def execute(self):
        con = PostgresConnection().getConnection()
        cur = con.cursor()
        select_query = "select s.division , sum(f.total_price)\
                        from ecomdb.fact_table f \
                        join ecomdb.store_dim s on s.store_key = f.store_key \
                        group by (s.division)\
                        order by s.division"
        cur.execute(select_query)
        records = cur.fetchall()
        query_1 = pd.DataFrame(list(records),columns = ['division','total_price'])
        query_1['total_price'] = query_1['total_price'].astype('float')
        #print(query_1)
        return query_1.to_dict(orient='records')

if __name__ == '__main__':
    q1 = Query1()
    data = q1.execute()
    print(data)