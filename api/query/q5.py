from api.database.dbcon import PostgresConnection
import pandas as pd
class Query5:
    def __init__(self):
        self.con = PostgresConnection().getConnection()
        print("Constructor called")

    def execute(self):
        con = PostgresConnection().getConnection()
        cur = con.cursor()
        select_stmt_bar2015 = "SELECT SUM(ft.total_price) " \
                              "FROM ecomdb_star_schema.fact_table ft " \
                              "JOIN ecomdb_star_schema.time_dim tim ON ft.time_key=tim.time_key " \
                              "JOIN ecomdb_star_schema.store_dim s ON ft.store_key=s.store_key " \
                              "WHERE s.division='BARISAL' AND tim.year=2015" \
                              "GROUP BY CUBE(s.division,tim.year)" \
                              "ORDER BY tim.year"
        cur.execute(select_stmt_bar2015)
        result = cur.fetchall()
        pd_data = pd.DataFrame(list(result), columns=['total_sales'])
        pd_data['total_sales'] = pd_data['total_sales'].astype('float64')
        pd_data = pd_data.dropna()
        # print(pd_data)
        return pd_data[:1].to_dict(orient='records')

if __name__ == '__main__':
    q5 = Query5()
    data = q5.execute()
    print(data)