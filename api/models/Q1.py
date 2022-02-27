from api.database.dbcon import PostgresConnection
import pandas as pd


class Query1:
    def __init__(self):
        # self.con = PostgresConnection.get_connection()
        print(" constructor called")

    def execute(self):
        select_stmt = " SELECT sr.division, SUM(fact.total_price) " \
                      " From ecomdb_star_schema.fact_table fact " \
                      " JOIN ecomdb_star_schema.store_dim sr on sr.store_key=fact.store_key "\
                      " GROUP BY (sr.division) " \
                      " ORDER BY sr.division"

        records = PostgresConnection.retrive_data_from_table(select_stmt)
        df = pd.DataFrame(list(records), columns=['division', 'total_sales'])
        return df.to_dict(orient='records')


# if __name__ == '__main__':
#     q1 = Query1()
#     data = q1.execute()
#     print(data)