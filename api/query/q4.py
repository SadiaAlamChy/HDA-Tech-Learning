from api.database.dbcon import PostgresConnection
import pandas as pd
class Query4:
    def __init__(self):
        self.con = PostgresConnection().getConnection()
        print("Constructor called")

    def execute(self):
        con = PostgresConnection().getConnection()
        cur = con.cursor()
        select_stmt_time2015 = "SELECT  SUM(ft.total_price) " \
                               "FROM ecomdb_star_schema.fact_table ft " \
                               "JOIN ecomdb_star_schema.time_dim tim ON ft.time_key=tim.time_key " \
                               "WHERE tim.year=2015 " \
                               "GROUP BY (tim.year)"
        cur.execute(select_stmt_time2015)
        result = cur.fetchall()
        pd_data = pd.DataFrame(list(result), columns=['total_sales'])
        pd_data['total_sales'] = pd_data['total_sales'].astype('float64')
        pd_data = pd_data.dropna()
        # print(pd_data)
        return pd_data.to_dict(orient='records')

if __name__ == '__main__':
    q4 = Query4()
    data = q4.execute()
    print(data)