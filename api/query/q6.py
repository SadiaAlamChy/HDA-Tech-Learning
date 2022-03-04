from database.dbcon import PostgresConnection
import pandas as pd


class Query6:
    def __init__(self):
        self.con = PostgresConnection().getConnection()
        print("Constructor called")

    def execute(self):
        con = PostgresConnection().getConnection()
        cur = con.cursor()
        select_stmt = "SELECT s.store_key, i.item_name, SUM(t.quantity) total_quantity " \
                      "From ecom_schema.fact_table t " \
                      "JOIN ecom_schema.store_dim s on s.store_key=t.store_key " \
                      "JOIN ecom_schema.item_dim i on i.item_key=t.item_key " \
                      "GROUP BY CUBE(s.store_key,i.item_name) "

        cur.execute(select_stmt)
        records = cur.fetchall()
        df = pd.DataFrame(list(records), columns=['store_key', 'item_name', 'total_quantity'])
        df = df.dropna()
        grouped = df.groupby(['store_key', 'item_name']).agg({'total_quantity': pd.Series.max})
        grouped
        #print(df)
        return grouped.to_dict(orient='records')


if __name__ == '__main__':
    q6 = Query6()
    data = q6.execute()
    print(data)
