from db.postgres import PostgresConnection
import pandas as pd

months = ['January', 'February', 'March', 'April',
          'May', 'June', 'July', 'August', 'September',
          'October', 'November', 'December']


class Query10:
    def __init__(self):
        self.con = PostgresConnection().get_connection()

    @staticmethod
    def execute():
        con = PostgresConnection().get_connection()
        cur = con.cursor()
        query = "select s.store_key, i.item_key, i.item_name, t.month, sum(f.total_price) " \
                "from star_schema.fact_table f " \
                "join star_schema.store_dim s on s.store_key = f.store_key " \
                "join star_schema.time_dim t on t.time_key = f.time_key " \
                "join star_schema.item_dim i on i.item_key = f.item_key " \
                "group by s.store_key, i.item_key, i.item_name, t.month " \
                "order by s.store_key, i.item_key, i.item_name, t.month " \
                "limit 20000"
        cur.execute(query)
        result = cur.fetchall()
        pd_data = pd.DataFrame(list(result), columns=['store', 'item_key', 'item_name', 'month', 'sum'])
        pd_data['sum'] = pd_data['sum'].astype('float64')
        stores = pd_data['store'].unique()
        store_list = []
        for store in stores:
            item_list = []
            all_items = pd_data[pd_data['store'] == store]
            unique_items = all_items['item_name'].unique()
            for u in unique_items:
                sales = []
                rows = pd_data[(pd_data['store'] == store) & (pd_data['item_name'] == u)]
                for i, j in rows.iterrows():
                    sales.append({'month': months[int(j['month']) - 1], 'total_sales': j['sum']})
                item_list.append({'item': u, 'sales': sales})
            store_list.append({'store': store, 'items': item_list})
        return store_list


if __name__ == '__main__':
    q = Query10()
    data = q.execute()
