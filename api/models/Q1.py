from api.database.dbcon import PostgresConnection
import pandas as pd


class Query1:
    def __init__(self):
        # self.con = PostgresConnection.get_connection()
        print(" constructor called")

    def execute(self):
        select_stmt = " SELECT sr.division ,sr.district,tim.month, tim.year, SUM(fact.total_price) " \
                      " From ecomdb_star_schema.fact_table fact " \
                      " JOIN ecomdb_star_schema.store_dim sr on sr.store_key=fact.store_key " \
                      " JOIN ecomdb_star_schema.time_dim tim on tim.time_key=fact.time_key " \
                      " GROUP BY (sr.division,sr.district,tim.month, tim.year) " \
                      " ORDER BY sr.division"

        records = PostgresConnection.retrive_data_from_table(select_stmt)
        df = pd.DataFrame(list(records), columns=['division', 'district', 'month', 'year', 'total_sales'])
        return df.to_dict(orient='records')


# if __name__ == '__main__':
#     q1 = Query1()
#     data = q1.execute()
#     print(data)