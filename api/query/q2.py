from api.database.dbcon import PostgresConnection
import pandas as pd
class Query2:
    def __init__(self):
        self.con = PostgresConnection().getConnection()
        print("Constructor called")

    def execute(self):
        con = PostgresConnection().getConnection()
        cur = con.cursor()
        select_stmt_transtype = "SELECT  tr.trans_type, SUM(ft.total_price)" \
                                "FROM ecomdb_star_schema.fact_table ft " \
                                "JOIN ecomdb_star_schema.trans_dim tr ON ft.payment_key=tr.payment_key " \
                                "GROUP BY CUBE(tr.trans_type) " \
                                "ORDER BY tr.trans_type"
        cur.execute(select_stmt_transtype)
        result = cur.fetchall()
        pd_data = pd.DataFrame(list(result), columns=['trans_type','total_sales'])
        pd_data['total_sales'] = pd_data['total_sales'].astype('float64')
        pd_data = pd_data.dropna()
        # print(pd_data)
        return pd_data.to_dict(orient='records')

if __name__ == '__main__':
    q2 = Query2()
    data = q2.execute()
    print(data)