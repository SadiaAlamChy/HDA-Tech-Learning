from api.database.dbcon import PostgresConnection
import pandas as pd


class Query8:
    def __init__(self):
        # self.con = PostgresConnection.get_connection()
        print(" constructor called")

    def execute(self):
        select_query = "select i.item_name, td.quarter, sum(f.quantity) " \
                       "from ecomdb_star_schema.fact_table f " \
                       "join ecomdb_star_schema.item_dim i on i.item_key=f.item_key " \
                       "join ecomdb_star_schema.time_dim td on td.time_key = f.time_key " \
                       "group by i.item_name, td.quarter " \
                       "order by i.item_name, sum(f.total_price)"

        record = PostgresConnection.retrive_data_from_table(select_query)
        df = pd.DataFrame(list(record), columns=['Item', 'Quarter', 'Total Quantity'])
        df = df.groupby('Item').head(1)
        df['Total Quantity'] = df['Total Quantity'].astype('int64')
        return df.to_dict(orient='records')

