from database.dbcon import PostgresConnection
import pandas as pd


class Query7:
    def __init__(self):
        self.con = PostgresConnection().getConnection()
        print("Constructor called")

    def execute(self):
        days = int(input('Enter no. of days for the query: '))
        con = PostgresConnection().getConnection()
        cur = con.cursor()
        select_stmt = "select  i.item_key, i.item_name,t.trans_type, tdim.dates " \
                      "From ecom_schema.fact_table f " \
                      "JOIN ecom_schema.trans_dim t on t.payment_key=f.payment_key " \
                      "JOIN ecom_schema.item_dim i on i.item_key=f.item_key " \
                      "JOIN ecom_schema.time_dim tdim on tdim.time_key = f.time_key " \
                      "WHERE (t.trans_type='card' or t.trans_type='mobile') and tdim.dates > (CURRENT_DATE - integer '{}')".format(
            days)
        cur.execute(select_stmt)
        result = cur.fetchall()
        df = pd.DataFrame(list(result), columns=["Item_key", "item_name", "Transaction Through", 'Date'])
        df = df.dropna()
        #print(df)
        return df.to_dict(orient='records')


if __name__ == '__main__':
    q7 = Query7()
    data = q7.execute()
    print(data)
