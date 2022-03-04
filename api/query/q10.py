from database.dbcon import PostgresConnection
import pandas as pd


class Query10:
    def __init__(self):
        self.con = PostgresConnection().getConnection()
        print("Constructor called")

    def execute(self):
        con = PostgresConnection().getConnection()
        cur = con.cursor()
        query = "select s.store_key, t.month, round(avg(f.total_price)::numeric,2) " \
                "from ecom_schema.fact_table f " \
                "join ecom_schema.store_dim s on s.store_key = f.store_key " \
                "join ecom_schema.time_dim t on t.time_key = f.time_key " \
                "where s.store_key = 'S00164' " \
                "group by s.store_key, t.month " \
                "order by s.store_key, t.month"
        cur.execute(query)
        result = cur.fetchall()
        df = pd.DataFrame(list(result), columns=['Store', 'Month', 'Avg. Sales'])
        #print(df)
        return df.to_dict(orient='records')


if __name__ == '__main__':
    q10 = Query10()
    data = q10.execute()
    print(data)
