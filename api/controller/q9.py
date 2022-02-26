from db.postgres import PostgresConnection
import pandas as pd


class Query9:
    def __init__(self):
        self.con = PostgresConnection().get_connection()

    @staticmethod
    def execute():
        con = PostgresConnection().get_connection()
        cur = con.cursor()
        query = "select i.item_name, s.division, sum(f.total_price) " \
                "from star_schema.fact_table f " \
                "join star_schema.item_dim i on i.item_key=f.item_key " \
                "join star_schema.store_dim s on s.store_key = f.store_key " \
                "where i.item_key ='I00082' " \
                "group by i.item_name, s.division " \
                "order by i.item_name,s.division"
        cur.execute(query)
        result = cur.fetchall()
        pd_data = pd.DataFrame(list(result), columns=['Item', 'Division', 'Sales'])
        pd_data['Sales'] = pd_data['Sales'].astype('float64')
        return pd_data.to_dict(orient='records')


if __name__ == '__main__':
    q = Query9()
    data = q.execute()
