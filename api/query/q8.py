from database.dbcon import PostgresConnection
import pandas as pd


class Query8:
    def __init__(self):
        self.con = PostgresConnection().getConnection()
        print("Constructor called")

    def execute(self):
        con = PostgresConnection().getConnection()
        cur = con.cursor()
        select_stmt = "WITH grouped_sales AS (SELECT quarter, item_key, SUM(quantity) AS total_quantity " \
                      "FROM ecom_schema.fact_table f join ecom_schema.Time_dim t ON t.time_key = f.time_key GROUP BY item_key,quarter) " \
                      "SELECT CONCAT(s.item_key, '->',s.quarter, '(',total_quantity,')') " \
                      "FROM grouped_sales s JOIN (SELECT item_key, min(total_quantity) AS minq " \
                      "FROM grouped_sales s GROUP BY item_key) ss ON ss.item_key = s.item_key and s.total_quantity = ss.minq "

        cur.execute(select_stmt)
        records = cur.fetchall()
        records
        df = pd.DataFrame(list(records), columns=['worst_season_for_each_item'])
        df = df.dropna()
        #print(df)
        return df.to_dict(orient='records')


if __name__ == '__main__':
    q8 = Query8()
    data = q8.execute()
    print(data)
