from db.postgres import PostgresConnection
import pandas as pd


class Query2:
    def __init__(self):
        self.con = PostgresConnection().get_connection()

    @staticmethod
    def execute():
        con = PostgresConnection().get_connection()
        cur = con.cursor()
        query = "select t.bank_name, sum(f.total_price) " \
                "from star_schema.fact_table f " \
                "join star_schema.trans_dim t on t.payment_key=f.payment_key " \
                "group by cube(t.bank_name) order by sum(f.total_price)"
        cur.execute(query)
        result = cur.fetchall()
        pd_data = pd.DataFrame(list(result), columns=['Bank', 'Sales'])
        pd_data['Sales'] = pd_data['Sales'].astype('float64')
        pd_data = pd_data.dropna()
        return pd_data.to_dict(orient='records')


if __name__ == '__main__':
    q = Query2()
    data = q.execute()
