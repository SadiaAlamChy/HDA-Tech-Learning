from database.dbcon import PostgresConnection
import pandas as pd


class Query2:
    def __init__(self):
        self.con = PostgresConnection().getConnection()
        print("Constructor called")

    def execute(self):
        con = PostgresConnection().getConnection()
        cur = con.cursor()
        query = "SELECT trs.trans_type, SUM(fact.total_price) " \
                " From ecom_schema.fact_table fact " \
                " JOIN ecom_schema.trans_dim trs on trs.payment_key = fact.payment_key " \
                " GROUP BY (trs.trans_type) "
        cur.execute(query)
        result = cur.fetchall()
        pd_data = pd.DataFrame(list(result), columns=['Trans_type', 'Total_sales'])
        pd_data['Total_sales'] = pd_data['Total_sales'].astype('float64')
        pd_data = pd_data.dropna()
        #print(pd_data)
        return pd_data.to_dict(orient='records')


if __name__ == '__main__':
    q2 = Query2()
    data = q2.execute()
    print(data)
