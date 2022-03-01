from database.dbcon import PostgresConnection
import pandas as pd
class Query10:
    def __init__(self):
        self.con = PostgresConnection().getConnection()
        print("Constructor called")

    def execute(self):
        con = PostgresConnection().getConnection()
        cur = con.cursor()
        query = " SELECT s.store_key ,tim.month,AVG(f.total_price) " \
                  " From ecomdb_star_schema.fact_table f " \
                  " JOIN ecomdb_star_schema.store_dim s on s.store_key=f.store_key " \
                  "JOIN ecomdb_star_schema.time_dim tim on tim.time_key=f.time_key " \
                  "Where s.store_key = 'S0001' " \
                  " GROUP BY (s.store_key,tim.month) "\
                  "ORDER BY tim.month"
        cur.execute(query)
        result = cur.fetchall()
        pd_data = pd.DataFrame(list(result), columns=['Store_key', 'Month', 'Average_Sales'])
        pd_data['Average_Sales'] = pd_data['Average_Sales'].astype('float64')
        return pd_data.to_dict(orient='records')

if __name__ == '__main__':
    q10 = Query10()
    data = q10.execute()
    print(data)