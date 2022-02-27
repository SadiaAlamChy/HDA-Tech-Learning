from api.database.dbcon import PostgresConnection
import pandas as pd


class Query6:
    def __init__(self):
        # self.con = PostgresConnection.get_connection()
        print(" constructor called")

    def execute(self):
        select_query = "select st.store_key, it.item_name, sum(fact.quantity) " \
                       "from ecomdb_star_schema.fact_table fact " \
                       "join ecomdb_star_schema.store_dim st on st.store_key = fact.store_key " \
                       "join ecomdb_star_schema.item_dim it on it.item_key = fact.item_key " \
                       "group by(st.store_key, it.item_key) " \
                       "order by st.store_key, sum(fact.quantity) desc"

        record = PostgresConnection.retrive_data_from_table(select_query)
        df = pd.DataFrame(list(record), columns=['Store', 'Item', 'Total Quantity'])
        df = df.dropna()
        df['Total Quantity'] = df['Total Quantity'].astype('int64')
        df = df.groupby('Store').head(4)

        return df.to_dict(orient='records')

