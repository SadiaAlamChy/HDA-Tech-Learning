from api.database.dbcon import PostgresConnection
import pandas as pd
class Query3:
    def __init__(self):
        self.con = PostgresConnection().getConnection()
        print("Constructor called")

    def execute(self):
        con = PostgresConnection().getConnection()
        cur = con.cursor()
        select_stmt_bari = "SELECT  SUM(ft.total_price) " \
                           "FROM ecomdb_star_schema.fact_table ft " \
                           "JOIN ecomdb_star_schema.store_dim s ON ft.store_key=s.store_key " \
                           "WHERE s.division='BARISAL' " \
                           "GROUP BY (s.division)"
        cur.execute(select_stmt_bari)
        result = cur.fetchall()
        pd_data = pd.DataFrame(list(result), columns=['total_sales'])
        pd_data['total_sales'] = pd_data['total_sales'].astype('float64')
        pd_data = pd_data.dropna()
        # print(pd_data)
        return pd_data.to_dict(orient='records')

if __name__ == '__main__':
    q3 = Query3()
    data = q3.execute()
    print(data)