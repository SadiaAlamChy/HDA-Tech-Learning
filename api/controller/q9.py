from flask import jsonify

from db.postgres import PostgresConnection
import pandas as pd


class Query9:
    def __init__(self):
        self.con = PostgresConnection().get_connection()

    @staticmethod
    def execute():
        con = PostgresConnection().get_connection()
        cur = con.cursor()
        query = "select i.item_key, i.item_name, s.division, sum(f.total_price) " \
                "from star_schema.fact_table f " \
                "join star_schema.item_dim i on i.item_key=f.item_key " \
                "join star_schema.store_dim s on s.store_key = f.store_key " \
                "group by i.item_key, i.item_name, s.division " \
                "order by i.item_key, i.item_name, s.division"
        cur.execute(query)
        result = cur.fetchall()
        pd_data = pd.DataFrame(list(result), columns=['key', 'item', 'division', 'sales'])
        pd_data['sales'] = pd_data['sales'].astype('float64')
        unique_items = pd_data['item'].unique()
        nested_list = []
        for u in unique_items:
            div_sales = []
            rows = pd_data[pd_data['item'] == u]
            for i, j in rows.iterrows():
                div_sales.append({'division': j['division'], 'total_sales': j['sales']})
            nested_list.append({'item': u, 'sales': div_sales})
        return nested_list


if __name__ == '__main__':
    q = Query9()
    data = q.execute()
