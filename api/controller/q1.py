from db.postgres import PostgresConnection
import pandas as pd


class Query1:
    def __init__(self):
        self.con = PostgresConnection().get_connection()

    @staticmethod
    def execute():
        con = PostgresConnection().get_connection()
        cur = con.cursor()
        query = "select s.division, sum(t.total_price) " \
                "from star_schema.fact_table t " \
                "join star_schema.store_dim s on s.store_key=t.store_key " \
                "group by cube(s.division)" \
                "order by s.division"
        cur.execute(query)
        result = cur.fetchall()
        pd_data = pd.DataFrame(list(result), columns=['division', 'sales'])
        pd_data['sales'] = pd_data['sales'].astype('float64')
        pd_data = pd_data.dropna()
        return pd_data.to_dict(orient='records')


if __name__ == '__main__':
    q1 = Query1()
    data = q1.execute()
