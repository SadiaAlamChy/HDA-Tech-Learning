from api.database.dbcon import PostgresConnection
import pandas as pd


class Query3:
    def __init__(self):
        # self.con = PostgresConnection.get_connection()
        print(" constructor called")

    def execute(self):
        select_stmt = "Select t2.division, sum(t1.total_price) " \
                       "from ecomdb_star_schema.fact_table t1 " \
                       "join ecomdb_star_schema.store_dim t2 on t1.store_key = t2.store_key " \
                       "where t2.division = 'BARISAL' " \
                       "group by(t2.division)"

        records = PostgresConnection.retrive_data_from_table(select_stmt)
        df = pd.DataFrame(list(records), columns=['division', 'total_sales'])
        return df.to_dict(orient='records')


