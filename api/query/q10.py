from api.database.dbcon import PostgresConnection
import pandas as pd
class Query10:
    def __init__(self):
        self.con = PostgresConnection().getConnection()
        print("Constructor called")

    def execute(self):
        con = PostgresConnection().getConnection()
        cur = con.cursor()
        select_avg = "SELECT s.store_key, tim.month, avg(ft.total_price) " \
                     "FROM ecomdb_star_schema.fact_table ft " \
                     "JOIN ecomdb_star_schema.store_dim s on s.store_key = ft.store_key " \
                     "JOIN ecomdb_star_schema.time_dim tim on tim.time_key = ft.time_key " \
                     "GROUP BY s.store_key, tim.month " \
                     "ORDER BY s.store_key, tim.month "
        cur.execute(select_avg)
        avg = cur.fetchall()
        avgmon = pd.DataFrame(list(avg), columns=['store_id', 'month', 'average_sales'])
        # print(pd_data)
        avgmon.set_index('store_id', inplace=True)
        return {"sales":avgmon.to_dict(orient='records')}
        #return avgmon.to_dict(orient='records')

if __name__ == '__main__':
    q10 = Query10()
    data = q10.execute()
    print(data)