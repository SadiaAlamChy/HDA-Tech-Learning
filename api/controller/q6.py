from db.postgres import PostgresConnection
import pandas as pd


class Query6:
    def __init__(self):
        self.con = PostgresConnection().get_connection()

    @staticmethod
    def execute():
        con = PostgresConnection().get_connection()
        cur = con.cursor()
        query = "select s.store_key, i.item_name, sum(f.quantity) " \
                "from star_schema.fact_table f " \
                "join star_schema.store_dim s on s.store_key=f.store_key " \
                "join star_schema.item_dim i on i.item_key=f.item_key " \
                "group by cube(s.store_key, i.item_name) " \
                "order by s.store_key, sum(f.quantity) desc"
        cur.execute(query)
        result = cur.fetchall()
        pd_data = pd.DataFrame(list(result), columns=['Store', 'Item', 'Total Quantity'])
        pd_data = pd_data.dropna()
        pd_data = pd_data.groupby('Store').head(3)
        # pd_data = pd_data.head(27)
        pd_data['Total Quantity'] = pd_data['Total Quantity'].astype('int64')
        # pd_data['Store/Item'] = pd_data['Store'] + ' / ' + pd_data['Item']
        return pd_data.to_dict(orient='records')


if __name__ == '__main__':
    q = Query6()
    data = q.execute()
