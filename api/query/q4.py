from database.dbcon import PostgresConnection
import pandas as pd


class Query4:
    def __init__(self):
        self.con = PostgresConnection().getConnection()
        print("Constructor called")

    def execute(self):
        con = PostgresConnection().getConnection()
        cur = con.cursor()
        select_stmt = "SELECT tim.year, SUM(t.total_price) Total_Sales " \
                      "FROM ecom_schema.fact_table t " \
                      "JOIN ecom_schema.time_dim tim ON t.time_key = tim.time_key " \
                      "WHERE tim.year = 2015 " \
                      "GROUP BY CUBE (tim.year)"
        cur.execute(select_stmt)
        records = cur.fetchall()
        df = pd.DataFrame(list(records), columns=['Year', 'total_sales_price'])
        #print(df)
        return df.to_dict(orient='records')


if __name__ == '__main__':
    q4 = Query4()
    data = q4.execute()
    print(data)
