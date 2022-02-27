from api.database.dbcon import PostgresConnection
import pandas as pd


class Query5:
    def __init__(self):
        # self.con = PostgresConnection.get_connection()
        print(" constructor called")

    def execute(self):
        select_stmt = "select t3.division, t2.year, sum(t1.total_price) " \
                       "from ecomdb_star_schema.fact_table t1 " \
                       "join ecomdb_star_schema.time_dim t2 on t1.time_key = t2.time_key " \
                       "join ecomdb_star_schema.store_dim t3 on t1.store_key = t3.store_key " \
                       "where  t2.year= 2015 and t3.division = 'BARISAL'  " \
                       "group by (t3.division, t2.year)"

        records = PostgresConnection.retrive_data_from_table(select_stmt)
        df = pd.DataFrame(list(records), columns=['division', 'year', 'total_sales'])
        return df.to_dict(orient='records')

