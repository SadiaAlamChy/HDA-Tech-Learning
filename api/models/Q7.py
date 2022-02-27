from api.database.dbcon import PostgresConnection
import pandas as pd



class Query7:
    def __init__(self, days):
        # self.con = PostgresConnection.get_connection()
        self.days = days
        print("Constructor called")


    def execute(self):
        select_stmt = "select distinct t3.item_name, sum(t1.quantity) " \
                      "from ecomdb_star_schema.fact_table t1 " \
                      "join ecomdb_star_schema.trans_dim t2 on t1.payment_key = t2.payment_key " \
                      "join ecomdb_star_schema.item_dim t3 on t1.item_key = t3.item_key " \
                      "join ecomdb_star_schema.time_dim t4 on t4.time_key = t1.time_key " \
                      "Where t4.date > (CURRENT_DATE - integer '{}') " \
                      "group by t3.item_name " \
                      "Order by sum(t1.quantity) desc ".format(int(self.days))

        records = PostgresConnection.retrive_data_from_table(select_stmt)
        df = pd.DataFrame(list(records), columns=['Item Name', 'Total Quantity'])
        return df.to_dict(orient='records')

