from database.dbcon import PostgresConnection
import pandas as pd


class Query5:
    def __init__(self):
        self.con = PostgresConnection().getConnection()
        print("Constructor called")

    def execute(self):
        con = PostgresConnection().getConnection()
        cur = con.cursor()
        select_stmt = "SELECT tim.year, s.division, SUM(t.total_price) Total_Sales " \
                      "FROM ecom_schema.fact_table t " \
                      "JOIN ecom_schema.store_dim s on s.store_key = t.store_key " \
                      "JOIN ecom_schema.time_dim tim ON t.time_key = tim.time_key " \
                      "WHERE s.division = 'BARISAL' and tim.year = 2015 " \
                      "GROUP BY ROLLUP (s.division, tim.year)"
        cur.execute(select_stmt)
        records = cur.fetchall()
        df = pd.DataFrame(list(records), columns=['year', 'division', 'total_sales_price'])
        df.drop([1, 2], axis=0, inplace=True)
        #print(df)
        return df.to_dict(orient='records')


if __name__ == '__main__':
    q5 = Query5()
    data = q5.execute()
    print(data)
