from db.postgres import PostgresConnection
import pandas as pd


class Query8:
    def __init__(self):
        self.con = PostgresConnection().get_connection()

    @staticmethod
    def execute():
        con = PostgresConnection().get_connection()
        cur = con.cursor()
        query = "select i.item_name, td.quarter, sum(f.total_price) " \
                "from star_schema.fact_table f " \
                "join star_schema.item_dim i on i.item_key=f.item_key " \
                "join star_schema.time_dim td on td.time_key = f.time_key " \
                "group by i.item_name, td.quarter " \
                "order by i.item_name, sum(f.total_price)"
        cur.execute(query)
        result = cur.fetchall()
        pd_data = pd.DataFrame(list(result), columns=['Item', 'Quarter', 'Sales'])
        pd_data = pd_data.dropna()
        pd_data = pd_data.groupby('Item').head(1)
        return pd_data.to_dict(orient='records')


if __name__ == '__main__':
    q = Query8()
    data = q.execute()
