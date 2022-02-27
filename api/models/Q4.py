from api.database.dbcon import PostgresConnection
import pandas as pd


class Query4:
    def __init__(self):
        # self.con = PostgresConnection.get_connection()
        print(" constructor called")

    def execute(self):
        select_stmt = "select  t2.year, sum(t1.total_price) " \
                       "from ecomdb_star_schema.fact_table t1 " \
                       "join ecomdb_star_schema.time_dim t2 on t1.time_key = t2.time_key " \
                       "where t2.year= 2015 " \
                       "group by(t2.year)"

        records = PostgresConnection.retrive_data_from_table(select_stmt)
        df = pd.DataFrame(list(records), columns=['Year', 'total_sales'])
        return df.to_dict(orient='records')
