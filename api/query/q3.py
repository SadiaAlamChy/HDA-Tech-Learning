from database.dbcon import PostgresConnection
import pandas as pd


class Query3:
    def __init__(self):
        self.con = PostgresConnection().getConnection()
        print("Constructor called")

    def execute(self):
        con = PostgresConnection().getConnection()
        cur = con.cursor()
        select_stmt = "SELECT s.district, SUM(t.total_price) Total_Sales " \
                      "FROM ecom_schema.fact_table t " \
                      "JOIN ecom_schema.store_dim s on s.store_key = t.store_key " \
                      "WHERE s.district = 'BARISAL' " \
                      "GROUP BY CUBE (s.district)"
        cur.execute(select_stmt)
        records = cur.fetchall()
        df = pd.DataFrame(list(records), columns=['district', 'total_sales_price'])
        df = df.dropna()
        #print(df)
        return df.to_dict(orient='records')


if __name__ == '__main__':
    q3 = Query3()
    data = q3.execute()
    print(data)
