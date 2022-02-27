from api.database.dbcon import PostgresConnection
import pandas as pd


class Query2:
    def __init__(self):
        # self.con = PostgresConnection.get_connection()
        print(" constructor called")

    def execute(self):
        select_stmt = " SELECT trs.trans_type, SUM(fact.total_price) " \
                      " From ecomdb_star_schema.fact_table fact " \
                      " JOIN ecomdb_star_schema.trans_dim trs on trs.payment_key = fact.payment_key " \
                      " GROUP BY (trs.trans_type) "

        records = PostgresConnection.retrive_data_from_table(select_stmt)
        df = pd.DataFrame(list(records), columns=['Trans type', 'Total sales'])
        return df.to_dict(orient='records')

