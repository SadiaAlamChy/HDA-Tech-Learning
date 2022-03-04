from database.dbcon import PostgresConnection
import pandas as pd


class Query9:
    def __init__(self):
        self.con = PostgresConnection().getConnection()
        print("Constructor called")

    def execute(self):
        con = PostgresConnection().getConnection()
        cur = con.cursor()
        query = "select i.item_name, s.division, sum(f.total_price) " \
                "from ecom_schema.fact_table f " \
                "join ecom_schema.item_dim i on i.item_key=f.item_key " \
                "join ecom_schema.store_dim s on s.store_key = f.store_key " \
                "where i.item_key ='I00082' " \
                "group by i.item_name, s.division " \
                "order by i.item_name,s.division"
        cur.execute(query)
        result = cur.fetchall()
        df = pd.DataFrame(list(result), columns=['Item', 'Division', 'Sales'])
        #print(df)
        return df.to_dict(orient='records')


if __name__ == '__main__':
    q9 = Query9()
    data = q9.execute()
    print(data)
